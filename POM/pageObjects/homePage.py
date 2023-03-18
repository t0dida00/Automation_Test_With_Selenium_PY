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
    div_items_class= "inventory_item"
    div_items_xpath='(//div[@class="inventory_item"])'
    div_item_image_xpath = '//div[@class="inventory_item_img"]'
    div_item_description_xpath = '//div[@class="inventory_item_description"]'
    div_item_label_xpath = '//div[@class="inventory_item_label"]'
    div_item_price_xpath = '//div[@class="inventory_item_price"]'
    button_add_to_cart_xpath="//button"
    button_add_to_cart_class="btn_inventory"
    button_twitter_class= "social_twitter"
    button_facebook_class = "social_facebook"
    button_linkedin_class = "social_linkedin"
    dropdown_sort_xpath ="//select[@class='product_sort_container']/option"
    links_social_xpath= "//ul[@class='social']/li/a"
    div_item_name_xpath='(//div[@class="inventory_item_name"])'
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

    def isAboutVisible(self):
        return self.driver.find_element(By.ID, self.a_link_about_id).is_displayed()


    def isLogOutVisible(self):
        return self.driver.find_element(By.ID, self.a_link_logout_id).is_displayed()


    def isResetAppVisible(self):
        return self.driver.find_element(By.ID, self.a_link_reset_app).is_displayed()


    def isItemSortVisible(self):
        return self.driver.find_element(By.CLASS_NAME, self.selection_product_sort_class).is_displayed()

    def clickItemSort(self):
         self.driver.find_element(By.CLASS_NAME, self.selection_product_sort_class).click()

    def countMethodsSort(self):
        return self.driver.find_elements(By.XPATH, self.dropdown_sort_xpath)
    def isMethodSortVisible(self,index):
        return self.driver.find_element(By.XPATH,self.dropdown_sort_xpath +'['+str(index)+']').is_displayed()
    def isItemsVisible(self):
        return self.driver.find_elements(By.CLASS_NAME,self.div_items_class)

    def isImageItemVisible(self,index):
        return self.driver.find_element(By.XPATH, self.div_items_xpath+'['+str(index)+']'+self.div_item_image_xpath).is_displayed()

    def isDescriptionVisible(self,index):
        return self.driver.find_element(By.XPATH, self.div_items_xpath + '[' + str(
            index) + ']' + self.div_item_description_xpath).is_displayed()

    def isItemPriceVisible(self,index):
        return self.driver.find_element(By.XPATH, self.div_items_xpath + '[' + str(
            index) + ']' + self.div_item_price_xpath).is_displayed()

    def isItemLabelVisible(self, index):
        return self.driver.find_element(By.XPATH, self.div_items_xpath + '[' + str(
            index) + ']' + self.div_item_label_xpath).is_displayed()

    def isAddtoCartButtonVisible(self, index):
        return self.driver.find_element(By.XPATH, self.div_items_xpath + '[' + str(
            index) + ']' + self.button_add_to_cart_xpath).is_displayed()

    def isTwitterVisible(self):
        return self.driver.find_element(By.CLASS_NAME,self.button_twitter_class).is_displayed()

    def isFacebookVisible(self):
        return self.driver.find_element(By.CLASS_NAME, self.button_facebook_class).is_displayed()

    def isLinkedinVisible(self):
        return self.driver.find_element(By.CLASS_NAME, self.button_linkedin_class).is_displayed()

    def getSocialLinks(self):
        return self.driver.find_elements(By.XPATH,self.links_social_xpath)

    def getAddtoCartButtons(self):
        return self.driver.find_elements(By.CLASS_NAME,self.button_add_to_cart_class)

    def clickImage(self,index):
         self.driver.find_element(By.XPATH, self.div_items_xpath + '[' + str(index) + ']' + self.div_item_image_xpath).click()

    def getImageSRC(self,index):
        return self.driver.find_element(By.XPATH, self.div_items_xpath + '[' + str(index) + ']' + self.div_item_image_xpath+ "//img").get_attribute("src")

    def getItemName(self,index):
        return self.driver.find_element(By.XPATH, self.div_item_name_xpath + '[' + str(index) + ']').get_attribute("textContent")

    def getItemPrice(self,index):
        return self.driver.find_element(By.XPATH, "("+self.div_item_price_xpath + ')[' + str(index) + ']').get_attribute("textContent")