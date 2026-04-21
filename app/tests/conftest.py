import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.main import app
from app.db.database import get_db
from httpx import AsyncClient
from httpx import ASGITransport
from app.core import config
import pytest_asyncio
import uuid


TEST_DB_URL = f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:5432/test_db"

engine = create_engine(TEST_DB_URL)
TestSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db():
    connection = engine.connect()
    transaction = connection.begin()
    session = TestSessionLocal(bind=engine)

    yield session 

    session.close()
    transaction.close()
    connection.close()


@pytest_asyncio.fixture
async def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest_asyncio.fixture
async def registered_user(client):
    user = {
        "name": "Ashik Aowal",
        "email": f"{uuid.uuid4()}@test.com",
        "role": "user",
        "password": "simplepassword"
    }

    response = await client.post("/auth/register", json=user)
    return user


@pytest_asyncio.fixture
async def auth_headers(client, registered_user):
    credentials = {
        "email": registered_user["email"],
        "password": registered_user["password"]
    }
    response = await client.post("/auth/login", json=credentials)
    headers = {
        "Authorization": f"Bearer {response.json()['access_token']}"
    }
    return headers


@pytest_asyncio.fixture
async def auth_headers_2(client):
    user = {
        "name": "User2",
        "email": f"{uuid.uuid4()}@test.com",
        "role": "user",
        "password": "password"
    }

    await client.post("/auth/register", json=user)

    response = await client.post("/auth/login", json={
        "email": user["email"],
        "password": user["password"]
    })

    headers = {
        "Authorization": f"Bearer {response.json()['access_token']}"
    }
    return headers


@pytest_asyncio.fixture
async def create_task(client, auth_headers):
    task = {
        "name": "Exercise",
        "description": "Do some stretching for 30 minutes or so",
        "is_completed": False,
        "due_date": "2026-04-26T09:03:18.633Z"
    }

    response = await client.post("/tasks/", headers=auth_headers, json=task)
    return response.json()






