import os
import pytest
from selenium import webdriver
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    #driver = webdriver.Chrome(ChromeDriverManager().install()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    return driver

"""@pytest.fixture()                                         ## to run the test on the browser sent in command prompt
def setup(browser):
    if browser=='edge':
        option = webdriver.EdgeOptions()
        driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options = option)
        print("Launching Edge browser.........")
    elif browser=='firefox':
        option = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(GeckoDriverManager().install(),options = option)
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install(),options = option)
        print("Launching chrome browser.........")
    return driver"""

# def pytest_adoption(parser):                       # this will get the value from command prompt
#     parser.addoption("--browser")


@pytest.fixture()
def browser(request):                                   # This will return the Browser value to setup method
    return request.config.getoption("--browser")

### To generate HTML report
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"