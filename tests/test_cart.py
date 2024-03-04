import pytest
from pages.cart_page import CartPage
from pages.checkoutOverview_page import CheckoutOverviewPage
from pages.checkoutYourInfo_page import YourInfoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.ordercomplete_page import OrderCompleted
from utilities.globalVars import globalVars


@pytest.mark.usefixtures('setup_teardown')
class TestCart:
    def test_add_product_to_cart(self):
        login_page = LoginPage()
        home_page = HomePage()
        login_page.perform_login(globalVars.user, globalVars.password)
        home_page.add_to_cart(globalVars.product_sauce_labs_backpack)

    def test_validate_products_in_cart(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        product1 = globalVars.product_sauce_labs_backpack
        product2 = globalVars.product_sauce_labs_bolt_tshirt
        login_page.perform_valid_login()
        home_page.add_to_cart(product1)
        home_page.go_to_cart()
        cart_page.validate_product_cart(product1)
        cart_page.click_continue_shopping()
        home_page.add_to_cart(product2)
        home_page.go_to_cart()
        cart_page.validate_product_cart(product1)
        cart_page.validate_product_cart(product2)

    def test_flow_add_products_to_cart_and_finish_checkout(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        checkout_your_info_page = YourInfoPage()
        checkout_overview_page = CheckoutOverviewPage()
        order_completed_page = OrderCompleted()
        expected_checkout_label = globalVars.checkout_label
        product1 = globalVars.product_sauce_labs_backpack
        product2 = globalVars.product_sauce_labs_bolt_tshirt
        login_page.perform_valid_login()
        checkout_fn = globalVars.first_name
        checkout_ls = globalVars.last_name
        checkout_pc = globalVars.postal_code
        checkout_overview_page_title = globalVars.checkout_overview_title
        completed_message = globalVars.completed_message
        home_page.add_to_cart(product1)
        home_page.go_to_cart()
        cart_page.validate_product_cart(product1)
        cart_page.click_continue_shopping()
        home_page.add_to_cart(product2)
        home_page.go_to_cart()
        cart_page.validate_product_cart(product1)
        cart_page.validate_product_cart(product2)
        cart_page.click_in_checkout()
        checkout_your_info_page.validate_correct_your_info_page(expected_checkout_label)
        checkout_your_info_page.fill_fields(checkout_fn,checkout_ls,checkout_pc)
        checkout_your_info_page.go_to_checkout_overview()
        checkout_overview_page.validate_checkout_overview_page(checkout_overview_page_title)
        checkout_overview_page.validate_product_cart_checkout(product1)
        checkout_overview_page.validate_product_cart_checkout(product2)
        checkout_overview_page.click_finish_btn()
        order_completed_page.validate_completed_message(completed_message)
