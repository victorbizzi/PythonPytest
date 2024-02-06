import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.globalVars import globalVars
#To run: python -v pytest tests/
#To run: pytest


@pytest.mark.usefixtures('setup_teardown')
class TestLogin:
    def test_SuccessfulLogin(self):
        login_page = LoginPage()
        home_page = HomePage()
        login_page.waitElementsLoad()
        login_page.performLogin(globalVars.user, globalVars.password)
        home_page.validateSuccessfulLogin()

    def test_UnsuccessfulLoginWrongPassword(self):
        login_page = LoginPage()
        login_page.performLogin(globalVars.user, "WrongPass12!")
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(globalVars.error_login_message_wrong_login)

    def test_UnsuccessfulLoginWrongUser(self):
        login_page = LoginPage()
        login_page.performLogin("IDontExist",globalVars.password)
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(globalVars.error_login_message_wrong_login)

    def test_UnsuccessfulLoginBlankPassword(self):
        login_page = LoginPage()
        login_page.performLogin(globalVars.user,"")
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(globalVars.error_login_message_password_required)

    def test_UnsuccessfulLoginBlankUsername(self):
        login_page = LoginPage()
        login_page.performLogin("", globalVars.password)
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(globalVars.error_login_message_username_required)

    def test_UnsuccessfulLoginBlankUsernameAndPassword(self):
        login_page = LoginPage()
        login_page.performLogin("","")
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(globalVars.error_login_message_username_required)

    def test_UnsuccessfulLoginLockedUser(self):
        login_page = LoginPage()
        login_page.performLogin(globalVars.locked_out_user,globalVars.password)
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(globalVars.error_login_message_locked_user)
