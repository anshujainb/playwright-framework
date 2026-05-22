from pages.base_page import BasePage

class InventoryPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.cart_badge= page.locator("[data-test='shopping-cart-badge']")
        self.shopping_cart_link=page.locator(".shopping_cart_link")
    
    #add to cart
    def add_product_to_cart(self, product_name):
        product_id= product_name.lower().replace(" ","-")
        locator = self.page.locator(
            f"[data-test='add-to-cart-{product_id}']"
        )

        self.click(locator)
    
    #click shopping cart link

    def get_cart_badge(self):
        return self.cart_badge
    
    def open_cart(self):
        self.click(self.shopping_cart_link)