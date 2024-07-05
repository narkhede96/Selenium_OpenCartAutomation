from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AccountRegistration:
    # locators
    chkbox_male_ID = "gender-male"
    chkbox_female_ID = "gender-female"
    txtbox_firstName_NAME = "FirstName"
    txtbox_lastName_NAME = "LastName"
    drpdwn_day_NAME = "DateOfBirthDay"
    drpdwn_month_NAME = "DateOfBirthMonth"
    drpdwn_year_NAME = "DateOfBirthYear"
    txtbox_Email_ID = "Email"
    txtbox_company_ID = "Company"
    txtbox_password_ID = "Password"
    txtbox_cnfrmpwd_ID = "ConfirmPassword"
    button_register_ID = "register-button"
    txt_regmsg_XPATH = "//div[@class='result']"

    def __init__(self,driver):
        self.driver = driver

    def selectGender(self,gender):
        self.male = self.driver.find_element(By.ID,self.chkbox_male_ID)
        self.female = self.driver.find_element(By.ID,self.chkbox_female_ID)

        if gender == "Male":
            self.male.click()
        else:
            self.female.click()

    def enterFirstName(self, first):
        self.first = self.driver.find_element(By.NAME, self.txtbox_firstName_NAME)
        self.first.send_keys(first)

    def enterLastName(self,last):
        self.last = self.driver.find_element(By.NAME,self.txtbox_lastName_NAME)
        self.last.send_keys(last)

    def selectDay(self,day):
        self.drpdwnday = self.driver.find_element(By.NAME,self.drpdwn_day_NAME)
        self.drpday = Select(self.drpdwnday)
        self.drpday.select_by_index(day)

    def selectMonth(self,month):
        self.drpdwnmonth = self.driver.find_element(By.NAME,self.drpdwn_month_NAME)
        self.drpmonth = Select(self.drpdwnmonth)
        self.drpmonth.select_by_visible_text(month)

    def selectYear(self,year):
        self.drpdwnyear = self.driver.find_element(By.NAME,self.drpdwn_year_NAME)
        self.drpyear = Select(self.drpdwnyear)
        self.drpyear.select_by_value(year)

    def enterEmail(self,email):
        self.email = self.driver.find_element(By.ID, self.txtbox_Email_ID)
        self.email.send_keys(email)

    def enterCompany(self,company):
        self.company = self.driver.find_element(By.ID, self.txtbox_company_ID)
        self.company.send_keys(company)

    def enterPassword(self,pwd):
        self.passwrd = self.driver.find_element(By.ID, self.txtbox_password_ID)
        self.passwrd.send_keys(pwd)

    def enterCnfmPassword(self,cfmpwd):
        self.cnfmpasswrd = self.driver.find_element(By.ID,self.txtbox_cnfrmpwd_ID )
        self.cnfmpasswrd.send_keys(cfmpwd)

    def clickRegister(self):
        self.driver.find_element(By.ID, self.button_register_ID).click()

    def getRegistrationMsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_regmsg_XPATH).text
        except:
            None






