import unittest
from selenium import webdriver
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.pageObjects.loginPage import LoginPage
from POM.pageObjects.homePage import HomePage
import HtmlTestRunner

sys.tracebacklimit = 0

__unittest = True


class SmokeTest(unittest.TestCase):
    baseURL = "https://www.saucedemo.com/"
    standard_user = "standard_user"
    password = "secret_sauce"

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

    def test_isTitleVisible(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        print(lg.isTitleVisible())
        self.assertEqual(True, lg.isTitleVisible())

    def test_isUsernameInputVisible(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        print(lg.isUsernameInputVisible())
        self.assertEqual(True, lg.isUsernameInputVisible())

    def test_isUsernameInputEnable(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        print(lg.isUsernameInputEnable())
        self.assertEqual(True, lg.isUsernameInputEnable())

    def test_isPasswordInputVisible(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        print(lg.isPasswordInputVisible())
        self.assertEqual(True, lg.isPasswordInputVisible())

    def test_isPasswordInputEnable(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        print(lg.isPasswordInputEnable())
        self.assertEqual(True, lg.isPasswordInputEnable())
    def isLoginButtonVisible(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        print(lg.isLoginButtonVisible())
        self.assertEqual(True, lg.isLoginButtonVisible())

    def test_isLoginButtonEnable(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        print(lg.isLoginButtonEnable())
        self.assertEqual(True, lg.isLoginButtonEnable())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
