from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class OrderCompleted(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.order_checkout_completed = (By.XPATH, "//h2[contains(text(),'Thank you for your order!')]")

    def validate_completed_message(self, text_message):
        text = self.validate_element_text(self.order_checkout_completed)
        assert text == text_message

