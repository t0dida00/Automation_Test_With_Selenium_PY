import time
import unittest
from selenium import webdriver
import sys
import os

from selenium.webdriver import Keys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.pageObjects.loginPage import LoginPage
from POM.pageObjects.homePage import HomePage
from selenium.webdriver.common.action_chains import ActionChains

sys.tracebacklimit = 0

__unittest = True

class LinksTest(unittest.TestCase):
    baseURL = "https://www.saucedemo.com/"
    standard_user = "standard_user"
    problem_user= "problem_user"
    password = "secret_sauce"
    homeURL = "https://www.saucedemo.com/inventory.html"
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        lg = LoginPage(cls.driver)
        lg.setUsername(cls.problem_user)
        lg.setPassword(cls.password)
        lg.clickLogin()
        cls.AddButtonsErrors = []
        cls.RemoveButtonsErrors = []
    def test_SocialLinks(self):
        hp = HomePage(self.driver)
        expect_links =["https://twitter.com/saucelabs","https://www.facebook.com/saucelabs","https://www.linkedin.com/company/sauce-labs/"]
        links = hp.getSocialLinks()
        for link in links:
            self.assertIn(link.get_attribute("href"),expect_links,"\nLink Error:" + link.get_attribute("href"))

    def test_AddtoCart_Activate(self):
        hp = HomePage(self.driver)
        addButtons = hp.getAddtoCartButtons()


        #check if add to cart buttons working or not
        for button in addButtons:
            button.click()
            afterClick =hp.getAddtoCartButtons()
            #try:self.assertEqual("Remove", afterClick[addButtons.index(button)].get_attribute("textContent"),addButtons.index(button))

            try:
                self.assertEqual("Remove", afterClick[addButtons.index(button)].get_attribute("textContent"),
                                 addButtons.index(button))
            except AssertionError as e:self.AddButtonsErrors.append(button.get_attribute("name"))
            #button.click
        # check if remove buttons working or not
        self.assertEqual([], self.AddButtonsErrors)
        addButtons = hp.getAddtoCartButtons()
        for button in addButtons:
            button.click()
            afterClick = hp.getAddtoCartButtons()
            try:
                self.assertEqual("Add to cart", afterClick[addButtons.index(button)].get_attribute("textContent"),
                                 addButtons.index(button))
            except AssertionError as e:
                self.RemoveButtonsErrors.append(button.get_attribute("name"))

        self.assertEqual([],self.RemoveButtonsErrors)

    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
