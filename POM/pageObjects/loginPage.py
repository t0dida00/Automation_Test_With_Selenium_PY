from selenium.webdriver.common.by import By


class LoginPage():
    textbox_username_id = "user-name"
    textbox_password_id ="password"
    button_login_id="login-button"
    tag_error_xpath = "//h3[@data-test='error']"
    text_title_class="login_logo"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
    def clickLogin(self):

        self.driver.find_element(By.ID,self.button_login_id).click()

    def getErrorInvaldAccount(self):
        return self.driver.find_element(By.XPATH,self.tag_error_xpath).get_attribute('textContent')

    def isTitleVisible(self):
        return self.driver.find_element(By.CLASS_NAME,self.text_title_class).is_displayed()

    def isUsernameInputVisible(self):
        return self.driver.find_element(By.ID,self.textbox_username_id).is_displayed()
    def isUsernameInputEnable(self):
        return self.driver.find_element(By.ID,self.textbox_username_id).is_enabled()

    def isPasswordInputVisible(self):
        return self.driver.find_element(By.ID, self.textbox_password_id).is_displayed()

    def isPasswordInputEnable(self):
        return self.driver.find_element(By.ID, self.textbox_password_id).is_enabled()
    def isLoginButtonVisible(self):
        return self.driver.find_element(By.ID, self.button_login_id).is_displayed()

    def isLoginButtonEnable(self):
        return self.driver.find_element(By.ID, self.button_login_id).is_enabled()
