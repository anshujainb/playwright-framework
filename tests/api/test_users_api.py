from utils.api_client import APIClient
from jsonschema import validate
from schemas.user_schema import user_schema
import pytest


def test_get_users(api_client):
    response = api_client.get("/users")
    data = response.json()
    assert data[0]["name"] == "Leanne Graham"
    assert response.status_code == 200


def test_create_post(api_client,auth_headers):

    

    payload = {
        "title": "Playwright",
        "body": "API Testing",
        "userId": 1
    }

    response = api_client.post("/posts",payload, auth_headers)
    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Playwright"

def test_update_post(api_client, auth_headers):
    payload = {
        "id" : 1,
        "title": "updated title",
        "body": "API Testing",
        "userId": 1
    }

    response = api_client.put("/posts/1",payload, auth_headers)
    assert response.status_code == 200
    data= response.json()
    assert data["title"] == "updated title"


def test_delete_post(api_client, auth_headers):

    response = api_client.delete("/posts/1", auth_headers)
    assert response.status_code == 200


def test_secure_api(api_client, auth_headers):
    

    response = api_client.get(
        "/secure-endpoint",
        headers=auth_headers
    )

@pytest.mark.parametrize("user_id, expected_name",
                         [
                             (1, "Leanne Graham"),
                             (2, "Ervin Howell")
                         ])
def test_user_names(api_client, user_id, expected_name):
    response = api_client.get(
        f"/users/{user_id}"
    )
    data = response.json()
    assert data["name"] == expected_name

def test_user_schema(api_client):
    response = api_client.get(f"/users/1")
    data = response.json()
    validate(
        instance=data,
        schema= user_schema

    )
