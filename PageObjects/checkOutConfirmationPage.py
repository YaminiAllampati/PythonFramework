from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utiles.BrowserUtiles import BrowserUtiles


class CheckOut_Confirmation_Page(BrowserUtiles):

    def __init__(self,driver):
        super().__init__(driver)  # calling BrowserUtiles class constructor
        self.driver=driver
        self.chckOut_Cfrm_btn=(By.XPATH, "//button[@class='btn btn-success']")
        self.country_text=(By.ID, "country")
        self.checkBox_btn=(By.XPATH, "//input[@id='checkbox2']")
        self.purchase_btn=(By.XPATH, "//input[@class='btn btn-success btn-lg']")
        self.confirm_msge=(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")





    def chckOut_Confirm(self):
        self.driver.find_element(*self.chckOut_Cfrm_btn).click()

    def location_select(self,country_name):
        self.driver.find_element(*self.country_text).send_keys(country_name)
        w = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='India']")))
        w.click()

        chk = self.driver.find_element(*self.checkBox_btn)
        if chk.is_selected():
            chk.click()
        self.driver.find_element(*self.purchase_btn).click()

    def confirmation_msge(self):

        msge = self.driver.find_element(*self.confirm_msge).text

        assert "Success! Thank you!" in msge

