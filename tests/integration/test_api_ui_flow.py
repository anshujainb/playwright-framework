from utils.api_client import APIClient
from playwright.sync_api import expect
def test_create_post_api_ui(api_client,auth_headers,page):
    payload = {
        "title": "Playwright",
        "body": "API Testing",
        "userId": 1
    }
    response = api_client.post("/posts",payload, auth_headers)
    assert response.status_code == 201

    data = response.json()

    post_id = data["id"]

    page.goto(f"https://jsonplaceholder.typicode.com/posts/{post_id}")

    expect(
        page.locator("body")
    ).to_contain_text(
        "Playwright"
    )
