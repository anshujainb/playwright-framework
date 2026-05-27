import pytest
import allure
from playwright.sync_api import expect

@pytest.mark.smoke
@pytest.mark.login

@allure.title("Verify login functionality")
@allure.description("User should login successfully")
def test_valid_login(login_page):

    
    # Verify successful login
    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    # Verify inventory page visible
   # expect(page.locator(".inventory_list")).to_be_visible()
   
@allure.title("login test failed")
def test_fail(page):
    page.goto("https://example.com")
    assert False