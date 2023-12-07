import pytest
from selenium import webdriver
driver: webdriver.Remote


@pytest.fixture()
def setup_teardown():
    # setup
    global driver
    url = "https://www.saucedemo.com/"
    # service_obj = Service()
    driver = webdriver.Chrome()  # service=service_obj)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    # Run
    yield
    # Teardown
    driver.close()
