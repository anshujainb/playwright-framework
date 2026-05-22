import pytest


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


