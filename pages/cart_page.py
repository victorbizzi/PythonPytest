from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.itemName = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.continueshoppingbtn = (By.ID, "continue-shopping")
        self.checkoutBtn = (By.ID, "checkout")

    def validateProductCart(self, item_name):
        item = (self.itemName[0], self.itemName[1].format(item_name))
        self.validateIfElementExists(item)

    def clickContinueShopping(self):
        self.waitElementAppears(self.continueshoppingbtn)
        self.clickAbstract(self.continueshoppingbtn)

    def clickInCheckout(self):
        self.waitElementAppears(self.checkoutBtn)
        self.clickAbstract(self.checkoutBtn)