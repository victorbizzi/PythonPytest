from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.item_name = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.continue_shopping_btn = (By.ID, "continue-shopping")
        self.checkout_btn = (By.ID, "checkout")

    def validate_product_cart(self, item_name):
        item = (self.item_name[0], self.item_name[1].format(item_name))
        self.validate_if_element_exists(item)

    def click_continue_shopping(self):
        self.wait_element_appears(self.continue_shopping_btn)
        self.click_abstract(self.continue_shopping_btn)

    def click_in_checkout(self):
        self.wait_element_appears(self.checkout_btn)
        self.click_abstract(self.checkout_btn)
