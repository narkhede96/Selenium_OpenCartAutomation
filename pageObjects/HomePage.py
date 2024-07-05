from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:
    # locators
    link_register_xpath = "//a[normalize-space()='Register']"
    link_login_xpath = "//a[normalize-space()='Log in']"                  # xpath for login link

    def __init__(self, driver):
        self.driver = driver

    def clickRegisterLink(self):
        self.driver.find_element(By.XPATH, self.link_register_xpath).click()

    def clickLoginLink(self):
        self.driver.find_element(By.XPATH, self.link_login_xpath).click()


