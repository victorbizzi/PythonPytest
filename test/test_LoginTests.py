import pytest
from selenium.webdriver.common.by import By
from .. import conftest


#@pytest.mark.usefixtures("setup_teardown")
#@pytest.mark.login
class TestLoginTests():
    def test_loginvalid(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()

    def test_Test(self):
        assert 1 == 1

    def test_TestA(self):
        assert 1 == 1

    def test_TestB(self):
        assert 1 == 1
