from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH, "//span[@class='title']")
        #self.iteminventory = (By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']")
        self.iteminventory = (By.XPATH, "//*[@class='inventory_item_name ' and text()='{}']") #usar string formatada para pegar item específico
        self.addtocartbtn = (By.XPATH,"//*[text()='Add to cart']")
        self.cartIcon = (By.XPATH, "//*[@class='shopping_cart_link']")

    def validateSuccessfulLogin(self):
        self.waitElementAppears(self.title_page)
        # WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='title']")))
        # assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()

    def validateElementHineoage(self):
        self.waitElementAppears(self.title_page)
    def addToCart(self, item_name):
        item = (self.iteminventory[0], self.iteminventory[1].format(item_name))  # By.XPATH é na posião [0], o XPATH (locator) está na posiçao [1], como o nome do item que queremos, ele tem que ter esse format para passar somente o que queremos
        self.clickAbstract(item)  # a variavel item montou um novo locator
        self.clickAbstract(self.addtocartbtn)

    def goToCart(self):
        self.clickAbstract(self.cartIcon)



'''
        self.

        "//div[@id='shopping_cart_container']/a/span")
        WebElement
        shoppingCartBadge1;

'''