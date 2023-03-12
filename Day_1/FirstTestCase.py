import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
driver.get("https://www.saucedemo.com/")

def login():
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    act_title=driver.title
    exp_title= "Swag Labs"
    if act_title ==exp_title:
        print("Login Test Passed")
    else:
        print("Login Test False")

login()

def purchase_process():
    driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']").click()
    act_quatity= driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']").text
    exp_quatity = 1
    if act_quatity == exp_quatity:
        print("Purchase Test Passed")
    else:
        print("Purchase Test False")
purchase_process()