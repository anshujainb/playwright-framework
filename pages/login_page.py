from pages.base_page import BasePage
class LoginPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
         #locators
        self.username_input = page.locator(
            "[data-test='username']"
        )

        self.password_input = page.locator(
            "[data-test='password']"
        )

        self.login_button = page.locator(
            "[data-test='login-button']"
        )


    #actions
    def load(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self,username,password):
        self.fill(
            self.username_input,
            username
        )
        self.fill(self.password_input, password)
        self.click(self.login_button)

        
