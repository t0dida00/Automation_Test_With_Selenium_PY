from selenium.webdriver.common.by import By


class HomePage():
    button_burger_id = "react-burger-menu-btn"

    text_title_class="app_logo"
    image_shopping_cart_id = "shopping_cart_container"
    selection_product_sort_class = "product_sort_container"
    a_link_all_items_id = "inventory_sidebar_link"
    a_link_about_id = "about_sidebar_link"
    a_link_reset_app = "reset_sidebar_link"
    a_link_logout_id = "logout_sidebar_link"
    def __init__(self,driver):
        self.driver=driver

    def clickHamburger(self):
        self.driver.find_element(By.ID,self.button_burger_id).click()

    def clickLogout(self):
        self.driver.find_element(By.ID,self.a_link_logout_id).click()

    def isTitleVisible(self):
        return self.driver.find_element(By.CLASS_NAME, self.text_title_class).is_displayed()


    def isShoppingCartVisible(self):
        return self.driver.find_element(By.ID,self.image_shopping_cart_id).is_displayed()

    def isHamburgerMenuVisible(self):
        return self.driver.find_element(By.ID,self.button_burger_id).is_displayed()
    def isHamburgerMenuEnable(self):
        return self.driver.find_element(By.ID,self.button_burger_id).is_displayed()

    def isAllItemsVisible(self):
        return self.driver.find_element(By.ID,self.a_link_all_items_id).is_displayed()
    def isAllItemsEnable(self):
        return self.driver.find_element(By.ID,self.a_link_all_items_id).is_enabled()

    def isAboutVisible(self):
        return self.driver.find_element(By.ID, self.a_link_about_id).is_displayed()

    def isAboutEnable(self):
        return self.driver.find_element(By.ID, self.a_link_about_id).is_enabled()

    def isLogOutVisible(self):
        return self.driver.find_element(By.ID, self.a_link_logout_id).is_displayed()

    def isLogOutEnable(self):
        return self.driver.find_element(By.ID, self.a_link_logout_id).is_enabled()

    def isResetAppVisible(self):
        return self.driver.find_element(By.ID, self.a_link_reset_app).is_displayed()

    def isResetAppEnable(self):
        return self.driver.find_element(By.ID, self.a_link_reset_app).is_enabled()

    def isItemSortVisible(self):
        return self.driver.find_element(By.CLASS_NAME, self.selection_product_sort_class).is_displayed()


