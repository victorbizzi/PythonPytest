from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[contains(text(),'Checkout: Overview')]")
        self.item_name_checkout = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.finish_btn = (By.ID, "finish")

    def validate_checkout_overview_page(self, text_title):
        text = self.validateElementText(self.page_title)
        assert text == text_title, f"Returned message was: '{text}', but the expected is: '{text_title}'."

    def validate_product_cart_checkout(self, item_name):
        item = (self.item_name_checkout[0], self.item_name_checkout[1].format(item_name))
        self.validateIfElementExists(item)

    def click_finish_btn(self):
        self.clickAbstract(self.finish_btn)