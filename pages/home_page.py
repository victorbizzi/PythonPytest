from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH, "//span[@class='title']")
        self.item_inventory = (By.XPATH, "//*[@class='inventory_item_name ' and text()='{}']") #usar string formatada para pegar item específico
        self.add_to_cart_btn = (By.XPATH,"//*[text()='Add to cart']")
        self.cart_icon = (By.XPATH, "//*[@class='shopping_cart_link']")

    def validate_successful_login(self):
        self.wait_element_appears(self.title_page)
        # WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='title']")))
        # assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()

    def validate_element_hineoage(self):
        self.wait_element_appears(self.title_page)

    def add_to_cart(self, item_name):
        item = (self.item_inventory[0], self.item_inventory[1].format(item_name))  # By.XPATH é na posião [0], o XPATH (locator) está na posiçao [1], como o nome do item que queremos, ele tem que ter esse format para passar somente o que queremos
        self.click_abstract(item)  # a variavel item montou um novo locator
        self.click_abstract(self.add_to_cart_btn)

    def go_to_cart(self):
        self.click_abstract(self.cart_icon)
