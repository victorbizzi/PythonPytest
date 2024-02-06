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
    def test_AddProductToCart(self):
        login_page = LoginPage()
        home_page = HomePage()
        login_page.performLogin(globalVars.user, globalVars.password)
        home_page.addToCart(globalVars.product_sauce_labs_backpack)

    def test_ValidateProductsInCart(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()

        product1 = globalVars.product_sauce_labs_backpack
        product2 = globalVars.product_sauce_labs_bolt_tshirt
        login_page.performValidLogin()
        home_page.addToCart(product1)
        home_page.goToCart()
        cart_page.validateProductCart(product1)
        cart_page.clickContinueShopping()
        home_page.addToCart(product2)
        home_page.goToCart()
        cart_page.validateProductCart(product1)
        cart_page.validateProductCart(product2)

    def test_FlowAddProductsToCartAndFinishCheckout(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        checkout_your_info_page = YourInfoPage()
        checkout_overview_page = CheckoutOverviewPage()
        order_completed_page = OrderCompleted()

        expected_checkout_label = globalVars.checkout_label
        product1 = globalVars.product_sauce_labs_backpack
        product2 = globalVars.product_sauce_labs_bolt_tshirt
        login_page.performValidLogin()
        checkout_fn = globalVars.first_name
        checkout_ls = globalVars.last_name
        checkout_pc = globalVars.postal_code
        checkout_overview_page_title = globalVars.checkoutOverview_title
        completed_message = globalVars.completed_message

        home_page.addToCart(product1)
        home_page.goToCart()
        cart_page.validateProductCart(product1)
        cart_page.clickContinueShopping()
        home_page.addToCart(product2)
        home_page.goToCart()
        cart_page.validateProductCart(product1)
        cart_page.validateProductCart(product2)
        cart_page.clickInCheckout()
        checkout_your_info_page.validateCorrectYourInfoPage(expected_checkout_label)
        checkout_your_info_page.fillFields(checkout_fn,checkout_ls,checkout_pc)
        checkout_your_info_page.goToCheckoutOvervieww()
        checkout_overview_page.validateCheckoutOverviewPage(checkout_overview_page_title)
        checkout_overview_page.validateProductCartCheckout(product1)
        checkout_overview_page.validateProductCartCheckout(product2)
        checkout_overview_page.clickFinishBtn()
        order_completed_page.validateCompletedMessage(completed_message)
