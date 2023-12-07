from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[contains(text(),'Checkout: Overview')]")
        self.item_name_checkout = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.finish_btn = (By.ID, "finish")

    def validateCheckoutOverviewPage(self, text_title):
        text = self.validateElementText(self.page_title)
        assert text == text_title, f"Returned message was: '{text}', but the expected is: '{text_title}'."

    def validateProductCartCheckout(self, item_name):
        item = (self.item_name_checkout[0], self.item_name_checkout[1].format(item_name))
        self.validateIfElementExists(item)

    def clickFinishBtn(self):
        self.clickAbstract(self.finish_btn)