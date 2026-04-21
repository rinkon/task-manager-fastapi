import pytest, pytest_asyncio

@pytest.mark.asyncio
async def test_get_user_tasks(client, auth_headers):
    response = await client.get("/tasks/", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["has_next"] == False
    assert len(response.json()["tasks"]) == 0


@pytest.mark.asyncio
async def test_create_task(client, auth_headers):
    task = {
        "name": "Exercise",
        "description": "Do some stretching for 30 minutes or so",
        "is_completed": False,
        "due_date": "2026-04-26T09:03:18.633Z"
    }

    response = await client.post("/tasks/", headers=auth_headers, json=task)
    
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_update_task(client, create_task, auth_headers):
    task_id = create_task["task"]["id"]
    task_body = {
        "is_completed": True
    }
    response = await client.patch("/tasks/" + str(task_id), headers=auth_headers, json=task_body)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_task(client, create_task, auth_headers):
    task_id = create_task["task"]["id"]
    response = await client.delete("/tasks/" + str(task_id), headers=auth_headers)
    assert response.status_code == 200
