import pytest
import os


from utils.api_client import (
    APIClient
)

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def auth_headers():
    headers = {
        "Authorization": "Bearer fake_token_123",
        "Content-Type": "application/json"
    }
    return headers

@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.load()
    login.login(
        "standard_user",
        "secret_sauce"
    )
    return login

@pytest.fixture
def inventory_page(login_page):
    inventory = InventoryPage(
        login_page.page
    )
    return inventory

@pytest.fixture
def cart_page(inventory_page):
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.open_cart()
    cart_page = CartPage(inventory_page.page)
    return cart_page

@pytest.fixture
def checkout_page(cart_page):
    cart_page.click_checkout_button()
    checkout_page = CheckoutPage(cart_page.page)
    return checkout_page

import os
import pytest
import allure


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        page = item.funcargs.get("page")

        if page:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_path = f"{screenshots_dir}/{item.name}.png"

            # 1. Take screenshot
            page.screenshot(path=screenshot_path)

            # 2. Attach to Allure report
            with open(screenshot_path, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            print(f"\nScreenshot saved + attached to Allure: {screenshot_path}")