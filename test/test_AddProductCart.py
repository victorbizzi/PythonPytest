import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestAddProduct:
    def test_add_products_Cart(self):
        driver = conftest.driver
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()
        assert driver.find_element(By.XPATH,"//span[@class='title']").is_displayed()
        driver.find_element(By.XPATH,"//a[@id='item_4_title_link']/div").click()
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID,"shopping_cart_container").click()