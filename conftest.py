import pytest
from selenium import webdriver
from utilities.globalVars import globalVars
driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():
    global driver
    driver = webdriver.Chrome()  # service=service_obj)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(globalVars.baseUrl)
    # Run
    yield
    # Teardown
    driver.close()
