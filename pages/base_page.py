import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def findElementAbstract(self, locator):
        return self.driver.find_element(*locator)

    def findMultipleElementsAbstract(self, locator):
        self.waitElementAppears(locator)
        return self.driver.find_element(*locator)

    def sendkeysAbstract(self, locator, text):
        self.waitElementAppears(locator)
        self.findElementAbstract(locator).send_keys(text)

    def clickAbstract(self, locator):
        self.waitElementAppears(locator)
        self.findElementAbstract(locator).click()

    def validateIfElementExists(self, locator):
        self.waitElementAppears(locator)
        assert self.findElementAbstract(locator).is_displayed(), f"Element '{locator}' has been not found!"

    def validateElementText(self, locator):
        self.waitElementAppears(locator)
        return self.findElementAbstract(locator).text

    def waitElementAppears(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def validateIfElementExists(self, locator):
        return self.findElementAbstract(locator), f"Element '{locator}' does not exist but it should exist"

    def validateIfElementDoesNotExiss(self, locator):
        assert len(self.findElementAbstract(locator)) == 0, f"Element '{locator}' does not exist but it should exist"

    def doubleClickAbstract(self, locator):
        element = self.waitElementAppears(locator)
        ActionChains(self.driver).double_click(element).perform()

    def rightClick(self, locator):
        element = self.waitElementAppears(locator)
        ActionChains(self.driver).context_click(element).perform()

    def pressKeyboardKeys(self, locator, key):
        element = self.findElementAbstract(locator)
        if key == "ENTER":
            element.send_keys(Keys.ENTER)
        elif key == "BACKSPACE":
            element.send_keys(Keys.BACKSPACE)