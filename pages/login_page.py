from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage
from utilities.globalVars import globalVars


class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID,  "user-name")
        self.password_field = (By.ID,  "password")
        self.login_btn = (By.ID,  "login-button")
        self.errorLoginMessage = (By.XPATH,"//h3")
        self.xIconUser = (By.CSS_SELECTOR,".form_group:nth-child(1) path")
        self.xIconPassword = (By.CSS_SELECTOR, ".form_group:nth-child(2) path")

    def performLogin(self, user, password):
        self.sendkeysAbstract(self.username_field, user)
        self.sendkeysAbstract(self.password_field,password)
        self.clickAbstract(self.login_btn)

    def performValidLogin(self):
        self.sendkeysAbstract(self.username_field, globalVars.user)
        self.sendkeysAbstract(self.password_field, globalVars.password)
        self.clickAbstract(self.login_btn)

    def validateErrorLoginMsg(self):
        self.validateIfElementExists(self.errorLoginMessage)

    def validateErrorLogin(self, expected_message):
        text_found =  self.validateElementText(self.errorLoginMessage)
        assert text_found == expected_message, f"Returned message was: '{text_found}', but the expected is: '{expected_message}'."

    def waitElementsLoad(self):
        self.waitElementAppears(self.username_field)
        self.waitElementAppears(self.password_field)