import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os
import openpyxl

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.pageObjects.loginPage import LoginPage
from POM.pageObjects.homePage import HomePage
import HtmlTestRunner

sys.tracebacklimit = 0

__unittest = True

"""
Test login by many types of accounts:
1: standard account
2: invalid account
3: block account
4: perfomance glitch account
5: problem account
"""


class LoginTest(unittest.TestCase):
    # Variables
    baseURL = "https://www.saucedemo.com/"
    standard_user = "standard_user"
    invalid_username_user = "invalid_username_user"
    locked_out_user = "locked_out_user"
    problem_user = "problem_user"
    performance_glitch_user = "performance_glitch_user"
    password = "secret_sauce"
    # bk = openpyxl.load_workbook("./POM/reports/Excel_report.xlsx")

    '''
    Pre testing: Setting webdriver for Chrome.
    '''

    @classmethod
    def setUpClass(cls):
        # cls.chr_options = Options()
        # cls.chr_options.add_experimental_option("detach", True)
        # cls.driver = webdriver.Chrome(options=cls.chr_options)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(2)

    '''
    Step 1: Go to URL.
    Step 2: Enter username: standard_user.
    Step 3: Enter password: secret_password.
    Step 4: Click on button Login.
    Step 5: verify url.
    Step 6: Click on Menu at the left side.
    Step 7: Click on button Logout
    '''

    def test_login_with_standard_user(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        lg.setUsername(self.standard_user)
        lg.setPassword(self.password)
        lg.clickLogin()
        act_url = self.driver.current_url
        exp_url = "https://www.saucedemo.com/inventory.html"
        self.assertEqual(exp_url, act_url)
        hp = HomePage(self.driver)
        hp.clickHamburger()
        hp.clickLogout()

    '''
    Step 1: Go to URL.
    Step 2: Enter username: locked_out_account.
    Step 3: Enter password: secret_password.
    Step 4: Click on button Login.
    Step 5: verify error message.
    '''

    def test_login_with_locked_out_user(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        lg.setUsername(self.locked_out_user)
        lg.setPassword(self.password)
        lg.clickLogin()
        act_error = lg.getErrorInvaldAccount()
        exp_error = "Epic sadface: Sorry, this user has been locked out."
        self.assertEqual(exp_error, act_error)

    '''
       Step 1: Go to URL.
       Step 2: Enter username: invalid_username_user.
       Step 3: Enter password: secret_password.
       Step 4: Click on button Login.
       Step 5: verify error message.
       '''
    def test_login_with_invalid_username_user(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        lg.setUsername(self.invalid_username_user)
        lg.setPassword(self.password)
        lg.clickLogin()
        act_error = lg.getErrorInvaldAccount()
        exp_error = "Epic sadface: Username and password do not match any user in this service"
        self.assertEqual(exp_error, act_error)

    # def test_login_with_performance_glitch_user(self, false=None):
    #     self.driver.get(self.baseURL)
    #     start = time.time()
    #     lg = LoginPage(self.driver)
    #     lg.setUsername(self.performance_glitch_user)
    #     lg.setPassword(self.password)
    #     lg.clickLogin()
    #     end = time.time()
    #
    #
    #     if end-start>2 :
    #         print(end-start)
    #         #self.assertFalse("Slow progress", false)
    #         pass
    #     act_url = self.driver.current_url
    #     exp_url = "https://www.saucedemo.com/inventory.html"
    #     self.assertEqual(exp_url, act_url)
    #     hp = HomePage(self.driver)
    #     hp.clickHamburger()
    #     hp.clickLogout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/AutomationTest/POM/reports"))
