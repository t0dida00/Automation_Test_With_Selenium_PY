from selenium.webdriver.common.by import By


class DetailPage():
    image_item_class = "inventory_details_img"
    item_name_class = "inventory_details_name"
    item_price_class= "inventory_details_price"
    def __init__(self, driver):
        self.driver = driver

    def getImageLink(self):
        return self.driver.find_element(By.CLASS_NAME, self.image_item_class).get_attribute("src")
    def getItemName(self):
        return self.driver.find_element(By.CLASS_NAME, self.item_name_class).get_attribute("textContent")
    def getItemPrice(self):
        return self.driver.find_element(By.CLASS_NAME, self.item_price_class).get_attribute("textContent")