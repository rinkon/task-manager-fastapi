import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_registration(client):
    user = {
        "name": "Ashik Aowal",
        "email": "r.aowal@gmail.com",
        "role": "user",
        "password": "simplepassword"
    }

    response = await client.post("/auth/register", json=user)

    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Registration Successful"



