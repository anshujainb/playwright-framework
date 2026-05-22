from playwright.sync_api import expect
import pytest
def test_cart_list_load(cart_page):
    expect(cart_page.get_cart_item("Sauce Labs Backpack")) .to_be_visible()
    expect(cart_page.get_cart_item("Sauce Labs Bike Light")) .to_be_visible()

@pytest.mark.regression
@pytest.mark.cart
def test_remove_item(cart_page):
    cart_page.remove_item("Sauce Labs Backpack")
    expect(cart_page.get_all_items_in_cart()).to_have_count(1)

    




