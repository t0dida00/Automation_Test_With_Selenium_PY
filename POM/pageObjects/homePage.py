from selenium.webdriver.common.by import By


class HomePage():
    button_burger_id = "react-burger-menu-btn"
    tag_logout_id="logout_sidebar_link"

    def __init__(self,driver):
        self.driver=driver

    def clickHamburger(self):
        self.driver.find_element(By.ID,self.button_burger_id).click()

    def clickLogout(self):
        self.driver.find_element(By.ID,self.tag_logout_id).click()
