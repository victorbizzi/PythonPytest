from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.itemName = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.continue_shopping_btn = (By.ID, "continue-shopping")
        self.checkout_btn = (By.ID, "checkout")

    def validate_product_cart(self, item_name):
        item = (self.itemName[0], self.itemName[1].format(item_name))
        self.validateIfElementExists(item)

    def click_continue_shopping(self):
        self.waitElementAppears(self.continue_shopping_btn)
        self.clickAbstract(self.continue_shopping_btn)

    def click_in_checkout(self):
        self.waitElementAppears(self.checkout_btn)
        self.clickAbstract(self.checkout_btn)