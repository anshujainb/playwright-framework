class CheckoutCompletePage:
    def __init__(self,page):
          self.page = page
          self.complete_header = page.locator("[data-test = 'complete-header']")

          
    def get_complete_message(self):

        return self.complete_header