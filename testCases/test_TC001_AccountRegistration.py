from datetime import time

from pageObjects.HomePage import HomePage
from pageObjects.registrationPage import AccountRegistration
from utilities import randomString
import os
from utilities.customLogger import LogGen


#from OpenCartAutomation.utilities.readProperties import readConfig


class TestAccountRegistration:
    #baseURL = readConfig.getApplicationURL()
    baseURL = "https://demo.nopcommerce.com/"
    logger= LogGen.loggen()                   # LogGen is class and loggen is method created inside it


    def test_accountRegistration(self, setup):
        self.logger.info("*** TC001_Registration started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("*** Launching the browser ***")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickRegisterLink()

        self.reg = AccountRegistration(self.driver)
        self.logger.info("*** Enter customer details ***")
        self.reg.selectGender("Female")
        self.reg.enterFirstName("Ana")
        self.reg.enterLastName("June")
        self.reg.selectDay(28)
        self.reg.selectMonth("May")
        self.reg.selectYear("1996")
        self.email = randomString.random_string_generator() + "@gmail.com"
        self.reg.enterEmail(self.email)
        self.reg.enterCompany("ABC")
        self.reg.enterPassword("abcdefg12")
        self.reg.enterCnfmPassword("abcdefg12")
        self.reg.clickRegister()
        time(5)
        self.confmsg = self.reg.getRegistrationMsg()
        if self.confmsg == "Your registration completed":
            self.logger.info("*** Registration is completed ***")
            assert True
        else:
            self.driver.save_screeenshots(os.path.abspath(os.curdir) + "\\screenshot\\" + "test_acc_reg.png")
            self.logger.info("*** Registration is failed ***")
            assert False




