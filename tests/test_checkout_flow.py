import pytest
from playwright.sync_api import expect
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

@pytest.mark.smoke
@pytest.mark.checkout
@pytest.mark.parametrize(
        "firstName,lastName,postalCode",
        [
            ("anu","james","123"),
            ("John", "Doe", "67890"),
            ("Sara", "Lee", "95035"),
        ]
        
)
def test_checkout(checkout_page,firstName,lastName,postalCode):
    
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout_page.fill_checkout_info(firstName,lastName,postalCode)
    checkout_overview_page = CheckoutOverviewPage(checkout_page.page)


    expect(checkout_overview_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(
        checkout_overview_page.page.locator(".cart_item")
    ).to_have_count(2)

    checkout_overview_page.click_finish_button()
    checkout_complete_page = CheckoutCompletePage(checkout_overview_page.page)

    expect(checkout_complete_page.get_complete_message()).to_have_text("Thank you for your order!")

@pytest.mark.regression
@pytest.mark.checkout
@pytest.mark.parametrize(
          "firstName,lastName,postalCode,error",
          [
               (
                "",
                "James",
                "12345",
                "Error: First Name is required"
                ),
                (
                "anu",
                "",
                "12345",
                "Error: Last Name is required"  
                ),
                ("anu",
                "James",
                "",
                "Error: Postal Code is required"
                )

          ]
)
def test_invalid_checkout(checkout_page,firstName,lastName,postalCode,error):
     expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
     checkout_page.fill_checkout_info(firstName,lastName,postalCode)
     expect(checkout_page.get_error_message()).to_have_text(error)


    
