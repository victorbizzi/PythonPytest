from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class YourInfoPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_yi = (By.CLASS_NAME,"title")
        self.first_name_txt = (By.ID, "first-name")
        self.last_name_txt = (By.ID, "last-name")
        self.postal_code_txt = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")

    def validate_correct_your_info_page(self, text):
        text_found = self.validate_element_text(self.title_yi)
        assert text_found == text, f"Returned message was: '{text_found}', but the expected is: '{text}'."

    def fill_fields(self, firstname, lastname, zipcode):
        self.sendkeys_abstract(self.first_name_txt, firstname)
        self.sendkeys_abstract(self.last_name_txt, lastname)
        self.sendkeys_abstract(self.postal_code_txt, zipcode)

    def go_to_checkout_overview(self):
        self.click_abstract(self.continue_btn)
