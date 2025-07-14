from selenium.webdriver.common.by import By

from PageObjects.shopPage import ShopPage
from Utiles.BrowserUtiles import BrowserUtiles


class LoginPage(BrowserUtiles):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.usrname_text= (By.NAME, "username")
        self.pswrd_text=(By.ID, "password")
        self.click_btn=(By.NAME, "signin")



    def login(self,username,password):
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        self.driver.find_element(*self.usrname_text).send_keys(username)
        self.driver.find_element(*self.pswrd_text).send_keys(password)
        self.driver.find_element(*self.click_btn).click()
        shop_Page=ShopPage(self.driver) #since we already know the next page is shop_page - we can directly call the object here
        return shop_Page
