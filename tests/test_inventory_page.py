from playwright.sync_api import expect
from pages.inventory_page import InventoryPage

# def test_inventory_page_loaded(inventory_page):
    
#     expect(
#         inventory_page
#     ).to_have_url(
#         "https://www.saucedemo.com/inventory.html"
#     )

def test_cart_badge(inventory_page):
     inventory_page.add_product_to_cart("Sauce Labs Backpack")
     expect(inventory_page.get_cart_badge()).to_have_text("1")
    



