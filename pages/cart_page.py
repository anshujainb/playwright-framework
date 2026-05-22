from pages.base_page import BasePage

class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = page.locator(
            "[data-test='checkout']"
        )
        self.cart_items = page.locator(".cart_item")
    
    #removeItem
    def get_all_items_in_cart(self):
        return self.cart_items
        
    def get_cart_item(self,product_name):
        return self.cart_items.filter(
        has_text=product_name
    )

    def remove_item(self,product_name):
        product_id= product_name.lower().replace(" ","-")
        locator = self.page.locator(f"[data-test='remove-{product_id}']")
        self.click(locator)


    #go_to_checkout

    def click_checkout_button(self):
        self.click(self.checkout_button)
        
        