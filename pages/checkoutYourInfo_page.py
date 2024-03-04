from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class YourInfoPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titleYI = (By.CLASS_NAME,"title")
        self.firstnameTxt = (By.ID, "first-name")
        self.lastnameTxt = (By.ID, "last-name")
        self.postalcodeTxt = (By.ID, "postal-code")
        self.continueBtn = (By.ID, "continue")


    def validate_correct_your_info_page(self, text):
        textfound = self.validateElementText(self.titleYI)
        assert textfound == text, f"Returned message was: '{textfound}', but the expected is: '{text}'."


    def fill_fields(self, firstname, lastname, zipcode):
        self.sendkeysAbstract(self.firstnameTxt, firstname)
        self.sendkeysAbstract(self.lastnameTxt, lastname)
        self.sendkeysAbstract(self.postalcodeTxt, zipcode)

    def go_to_checkout_overview(self):
        self.clickAbstract(self.continueBtn)
