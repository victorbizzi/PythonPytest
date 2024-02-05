import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.globalVars import globalVars
#To run: python -v pytest tests/
#To run: pytest


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
class TestLogin:
    def test_SuccessfulLogin(slef):
        login_page = LoginPage()
        home_page = HomePage()
        login_page.waitElementsLoad()
        login_page.performLogin(globalVars.user, globalVars.password)
        home_page.validateSuccessfulLogin()

    def test_UnsuccessfulLoginWrongPassword(self):
        expected_error_message = "Epic sadface: Username and password do not match any user in this service"
        login_page = LoginPage()
        login_page.performLogin(globalVars.user, "WorngPass12!")
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(expected_error_message)

    def test_UnsuccessfulLoginWrongUser(self):
        expected_error_message = "Epic sadface: Username and password do not match any user in this service"
        login_page = LoginPage()
        login_page.performLogin("IDontExixt",globalVars.password)
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(expected_error_message)

    def test_UnsuccessfulLoginBlankPassword(self):
        expected_error_message = "Epic sadface: Password is required"
        login_page = LoginPage()
        login_page.performLogin(globalVars.user,"")
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(expected_error_message)

    def test_UnsuccessfulLoginBlankUsername(self):
        expected_error_message = "Epic sadface: Username is required"
        login_page = LoginPage()
        login_page.performLogin("", globalVars.password)
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(expected_error_message)

    def test_UnsuccessfulLoginBlankUsernameAndPassword(self):
        expected_error_message = "Epic sadface: Username is required"
        login_page = LoginPage()
        login_page.performLogin("","")
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(expected_error_message)

    def test_UnsuccessfulLoginLockedUser(self):
        expected_error_message = "Epic sadface: Sorry, this user has been locked out."
        login_page = LoginPage()
        login_page.performLogin(globalVars.locked_out_user,globalVars.password)
        login_page.validateErrorLoginMsg()
        login_page.validateErrorLogin(expected_error_message)

