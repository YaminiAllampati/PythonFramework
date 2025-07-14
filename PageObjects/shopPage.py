from selenium.webdriver.common.by import By

from PageObjects.checkOutConfirmationPage import CheckOut_Confirmation_Page
from Utiles.BrowserUtiles import BrowserUtiles


class ShopPage(BrowserUtiles):
    def __init__(self,driver):
        super().__init__(driver) #calling BrowserUtiles class constructor
        self.driver=driver

        self.home_btn=(By.XPATH, "//a[text()='Shop']")
        self.all_prdctLinks=(By.XPATH, "//div[@class='card-body']/h4/a")

        self.chckOut_btn=(By.XPATH, "//a[@class='nav-link btn btn-primary']")


    def AddToCart(self, product_name):

          self.driver.find_element(*self.home_btn).click()

          prds = self.driver.find_elements(*self.all_prdctLinks)

          for prd in prds:
           # print(prd.text)
            if prd.text == product_name:#"Samsung Note 8":
               # driver.find_element(By.XPATH,"(//button[@class='btn btn-info'])[2]").click()
               prd.find_element(By.XPATH, "(//button[@class='btn btn-info'])").click()


    def checkout(self):
           self.driver.find_element(*self.chckOut_btn).click()
           chckout_page=CheckOut_Confirmation_Page(self.driver)
           return chckout_page


