import time
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


class LoginPageTest(unittest.TestCase):
    baseURL = "https://www.saucedemo.com/"
    standard_user = "standard_user"
    password = "secret_sauce"
    homeURL = "https://www.saucedemo.com/inventory.html"

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
        self.assertEqual(True, lg.isTitleVisible())

    def test_isUsernameInputVisible(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        self.assertEqual(True, lg.isUsernameInputVisible())

    def test_isUsernameInputEnable(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        self.assertEqual(True, lg.isUsernameInputEnable())

    def test_isPasswordInputVisible(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        self.assertEqual(True, lg.isPasswordInputVisible())

    def test_isPasswordInputEnable(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        self.assertEqual(True, lg.isPasswordInputEnable())

    def test_isLoginButtonVisible(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        self.assertEqual(True, lg.isLoginButtonVisible())

    def test_isLoginButtonEnable(self):
        self.driver.get(self.baseURL)
        lg = LoginPage(self.driver)
        self.assertEqual(True, lg.isLoginButtonEnable())

    '''
       Step 1: Go to URL.
       Step 2: Enter username: standard_user.
       Step 3: Enter password: secret_password.
       Step 4: Click on button Login.
       Step 5: verify url.
       Step 6: Click on Menu at the left side.
       Step 7: Click on button Logout
       '''

    # def test_login_logout_with_standard_user(self):
    #     self.driver.get(self.baseURL)
    #     lg = LoginPage(self.driver)
    #     lg.setUsername(self.standard_user)
    #     lg.setPassword(self.password)
    #     lg.clickLogin()
    #     act_url = self.driver.current_url
    #     exp_url = "https://www.saucedemo.com/inventory.html"
    #     self.assertEqual(exp_url, act_url)
    #     hp = HomePage(self.driver)
    #     hp.clickHamburger()
    #     hp.clickLogout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class HomePageTest(unittest.TestCase):
    baseURL = "https://www.saucedemo.com/"
    standard_user = "standard_user"
    password = "secret_sauce"
    homeURL = "https://www.saucedemo.com/inventory.html"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

        cls.driver.get(cls.baseURL)
        lg = LoginPage(cls.driver)
        lg.setUsername(cls.standard_user)
        lg.setPassword(cls.password)
        lg.clickLogin()
        act_url = cls.driver.current_url
        exp_url = "https://www.saucedemo.com/inventory.html"
        cls().assertEqual(exp_url, act_url)

    def test_isLogoVisible(self):
        hp = HomePage(self.driver)
        self.assertEqual(True,hp.isTitleVisible())
    def test_isLogoVisible(self):
        hp = HomePage(self.driver)
        self.assertEqual(True,hp.isTitleVisible())

    def test_isShoppingCartVisible(self):
        hp = HomePage(self.driver)
        self.assertEqual(True,hp.isShoppingCartVisible())

    def test_isHamburgerMenuEnable(self):
        hp = HomePage(self.driver)
        self.assertEqual(True,hp.isHamburgerMenuEnable())

    def test_isHamburgerMenuVisible(self):
        hp = HomePage(self.driver)
        self.assertEqual(True, hp.isHamburgerMenuVisible())

    def test_isItemSortVisible(self):
        hp = HomePage(self.driver)
        self.assertEqual(True, hp.isItemSortVisible())

    def test_ElementsInHamburgerMenuVisible(self):
        hp = HomePage(self.driver)

        hp.clickHamburger()
        time.sleep(1)
        self.assertEqual(True, hp.isAllItemsVisible(),"All Items invisible")
        self.assertEqual(True, hp.isAboutVisible(),"About invisible")
        self.assertEqual(True, hp.isLogOutVisible(),"Logout invisible")
        self.assertEqual(True, hp.isResetAppVisible(),"sResetApp invisible")
        self.assertEqual(True, hp.isAllItemsEnable(),"All Items disable")
        self.assertEqual(True, hp.isAboutEnable(),"About disable")
        self.assertEqual(True, hp.isLogOutEnable(),"Logout disable")
        self.assertEqual(True, hp.isResetAppEnable(),"Reset disable")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# def suite():
#     test_suite = unittest.TestSuite()
#     test_suite.addTest((HomePageTest("test_all_elements_in_home_page")))
#
#     return test_suite
#
#
# mySuite = suite()
#
# runner = unittest.TextTestRunner()
#
# runner.run(mySuite)
if __name__ == '__main__':
    unittest.main()