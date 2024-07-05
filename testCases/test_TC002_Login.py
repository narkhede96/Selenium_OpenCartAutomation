from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import AccountLogin
from utilities.customLogger import LogGen
import os


class Test_Login():
    baseURL = "https://demo.nopcommerce.com/"



    def test_login(self,setup):
        #self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickLoginLink()

        self.lp = AccountLogin(self.driver)
        self.lp.enterEmail("abc@gmail.com")
        self.lp.enterPassword("Vaishnavi")
        self.lp.clickLogin()

        self.targetPage = self.lp.isMyAccountPageExists()
        if self.targetPage == True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login")
            assert False


        self.driver.close()
        #self.logger.info("******* End of test_002_login **********")






