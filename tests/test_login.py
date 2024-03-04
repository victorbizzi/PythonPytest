import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.globalVars import globalVars
#To run: python -v pytest wwwww/
#To run: pytest


@pytest.mark.usefixtures('setup_teardown')
class TestLogin:
    def test_successful_login(self):
        login_page = LoginPage()
        home_page = HomePage()
        login_page.wait_elements_load()
        login_page.perform_login(globalVars.user, globalVars.password)
        home_page.validate_successful_login()

    def test_unsuccessful_login_wrong_password(self):
        login_page = LoginPage()
        login_page.perform_login(globalVars.user, "WrongPass12!")
        login_page.validate_error_login_msg()
        login_page.validate_error_login(globalVars.error_login_message_wrong_login)

    def test_unsuccessful_login_wrong_user(self):
        login_page = LoginPage()
        login_page.perform_login("IDontExist",globalVars.password)
        login_page.validate_error_login_msg()
        login_page.validate_error_login(globalVars.error_login_message_wrong_login)

    def test_unsuccessful_login_blank_password(self):
        login_page = LoginPage()
        login_page.perform_login(globalVars.user,"")
        login_page.validate_error_login_msg()
        login_page.validate_error_login(globalVars.error_login_message_password_required)

    def test_unsuccessful_login_blank_username(self):
        login_page = LoginPage()
        login_page.perform_login("", globalVars.password)
        login_page.validate_error_login_msg()
        login_page.validate_error_login(globalVars.error_login_message_username_required)

    def test_unsuccessful_login_blank_username_and_password(self):
        login_page = LoginPage()
        login_page.perform_login("","")
        login_page.validate_error_login_msg()
        login_page.validate_error_login(globalVars.error_login_message_username_required)

    def test_unsuccessful_login_locked_user(self):
        login_page = LoginPage()
        login_page.perform_login(globalVars.locked_out_user,globalVars.password)
        login_page.validate_error_login_msg()
        login_page.validate_error_login(globalVars.error_login_message_locked_user)
