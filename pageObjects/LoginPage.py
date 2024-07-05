from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AccountLogin:
    txtbox_email_ID ="Email"
    txtbox_password_ID = "Password"
    button_Login_xpath = "//button[normalize-space()='Log in']"
    msg_MyAccount_xpath = "//a[@class='ico-account']"

    def __init__(self, driver):
        self.driver = driver

    def enterEmail(self,email):
        self.driver.find_element(By.ID, self.txtbox_email_ID).send_keys(email)

    def enterPassword(self,pwd):
        self.driver.find_element(By.ID, self.txtbox_password_ID).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_MyAccount_xpath).is_displayed()
        except:
            return False
