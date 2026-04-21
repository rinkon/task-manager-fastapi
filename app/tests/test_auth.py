import pytest
import pytest_asyncio
import uuid

@pytest.mark.asyncio
async def test_registration(client):
    user = {
        "name": "Ashik Aowal",
        "email": f"{uuid.uuid4()}@test.com",
        "role": "user",
        "password": "simplepassword"
    }

    response = await client.post("/auth/register", json=user)

    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Registration Successful"


@pytest.mark.asyncio
async def test_login(client, registered_user):
    credentials = {
        "email": registered_user["email"],
        "password": registered_user["password"]
    }

    response = await client.post("/auth/login", json=credentials)

    assert response.status_code == 200

    assert response.json()["type"] == "bearer"


@pytest.mark.asyncio
async def test_authentication(client):
    response = await client.get("/tasks/")
    assert response.status_code == 401
    

@pytest.mark.asyncio
async def test_authorization(client, create_task, auth_headers_2):
    task_id = create_task["task"]["id"]
    
    response = await client.get("/tasks/" + str(task_id), headers=auth_headers_2)
    assert response.status_code == 403
    
    task_body = {
        "is_completed": True
    }

    response = await client.patch("/tasks/" + str(task_id), headers=auth_headers_2, json=task_body)
    assert response.status_code == 403

    response = await client.delete("/tasks/" + str(task_id), headers=auth_headers_2)
    assert response.status_code == 403

    


