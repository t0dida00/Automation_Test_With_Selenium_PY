import time
import unittest
from selenium import webdriver
import sys
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from POM.pageObjects.detailPage import DetailPage
from POM.pageObjects.loginPage import LoginPage
from POM.pageObjects.homePage import HomePage

sys.tracebacklimit = 0

__unittest = True

class DetailPageTest(unittest.TestCase):

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
        lg.setUsername(cls.standard_user)
        lg.setPassword(cls.password)
        lg.clickLogin()
        cls.LinkData=["https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg",
                         "https://www.saucedemo.com/static/media/bike-light-1200x1500.37c843b0.jpg",
                         "https://www.saucedemo.com/static/media/bolt-shirt-1200x1500.c2599ac5.jpg",
                         "https://www.saucedemo.com/static/media/sauce-pullover-1200x1500.51d7ffaf.jpg",
                         "https://www.saucedemo.com/static/media/red-onesie-1200x1500.2ec615b2.jpg",
                         "https://www.saucedemo.com/static/media/red-tatt-1200x1500.30dadef4.jpg"]
        cls.LinkError=[]

    @classmethod
    def setUp(self):
        self.LinkError = []
    def test_isMatchingImage_Homepage(self):
        dp=DetailPage(self.driver)
        hp=HomePage(self.driver)

        items = len(hp.isItemsVisible())

        for item in range(1,items+1):
            if hp.getImageSRC(item) not in self.LinkData:
                self.LinkError.append(hp.getImageSRC(item))
        self.assertEqual([],self.LinkError)

    def test_isMatchingImage_Detailpage(self):
        dp = DetailPage(self.driver)
        hp = HomePage(self.driver)

        items = len(hp.isItemsVisible())

        for item in range(1, items + 1):
            image_homepage= hp.getImageSRC(item)
            hp.clickImage(item)
            image_detailpage = dp.getImageLink()
            if image_detailpage != image_homepage:
                self.LinkError.append(image_detailpage)
            self.driver.find_element(By.ID,"back-to-products").click()
        self.assertEqual([], self.LinkError)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()