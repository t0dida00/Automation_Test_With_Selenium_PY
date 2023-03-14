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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class HomePageTest(unittest.TestCase):
    baseURL = "https://www.saucedemo.com/"
    standard_user = "standard_user"
    problem_user="problem_user"
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

    def test_ElementsOfLandingPageVisible(self):
        hp = HomePage(self.driver)
        self.assertEqual(True, hp.isTitleVisible())
        self.assertEqual(True, hp.isTitleVisible())
        self.assertEqual(True, hp.isShoppingCartVisible())
        self.assertEqual(True, hp.isHamburgerMenuEnable())
        self.assertEqual(True, hp.isHamburgerMenuVisible())
        self.assertEqual(True, hp.isItemSortVisible())
        items = len(hp.isItemsVisible())
        self.assertEqual(True, items >0 , "Items Invisible")
        for item in range (1,items+1):
            self.assertEqual(True, hp.isImageItemVisible(item), "Item images invisible")
            self.assertEqual(True, hp.isDescriptionVisible(item), "Item descriptions invisible")
            self.assertEqual(True, hp.isItemPriceVisible(item), "Item price invisible")
            self.assertEqual(True, hp.isItemLabelVisible(item), "Item label invisible")
            self.assertEqual(True, hp.isAddtoCartButtonVisible(item), "Add button invisible")
        self.assertEqual(True, hp.isTwitterVisible())
        self.assertEqual(True, hp.isFacebookVisible())
        self.assertEqual(True, hp.isLinkedinVisible())
    def test_ElementsInHamburgerMenuVisible(self):
        hp = HomePage(self.driver)

        hp.clickHamburger()
        time.sleep(1)
        self.assertEqual(True, hp.isAllItemsVisible(),"All Items invisible")
        self.assertEqual(True, hp.isAboutVisible(),"About invisible")
        self.assertEqual(True, hp.isLogOutVisible(),"Logout invisible")
        self.assertEqual(True, hp.isResetAppVisible(),"sResetApp invisible")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()