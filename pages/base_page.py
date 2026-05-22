class BasePage:
    def __init__(self,page):
        self.page = page

    def fill(self, locator,text):
        locator.fill(text)
    
    def get_text(self, locator):

        return locator.text_content()
    
    def click(self, locator):

        locator.click()