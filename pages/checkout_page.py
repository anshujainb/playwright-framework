from pages.base_page import BasePage

class CheckoutPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.first_name= page.locator("[data-test='firstName']")
        self.last_name= page.locator("[data-test='lastName']")
        self.postal_code=page.locator("[data-test='postalCode']")
        self.submit_button = page.locator(
            "[data-test='continue']"
        )
        self.error_msg= page.locator("[data-test='error']")

    def fill_checkout_info(self,firstName,lastName,postalCode):
        self.fill(self.first_name,firstName)
        self.fill(self.last_name,lastName)
        self.fill(self.postal_code,postalCode)
        self.click(self.submit_button)
    
    def get_error_message(self):
        return self.error_msg