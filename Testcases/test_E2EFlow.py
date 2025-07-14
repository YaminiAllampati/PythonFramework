import json

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.login import LoginPage
from PageObjects.shopPage import ShopPage, ShopPage
from conftest import setup

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
testdata_path = os.path.join(current_dir, "..", "TestData", "test_data.json")

#testdata_path="../TestData/test_data.json"
with open(testdata_path,'r') as file:
   testdata=json.load(file)
#the json has converted to dictionary
#extract the data from json
   test_list=testdata["data"]
   #username = testdata["data"][0]["username"]

   """for d in testdata["data"]:
        username=d["username"]
        password=d["password"]
        product_name=d["product_name"]"""

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_items",test_list) #test_list returning list of data, and at each iterate it will give index[0] data to items and pass it to the code
def test_e2e(setup,test_list_items,pass_Url): #def test_e2e(setup,test_list_items,pass_Url):
  driver=setup #calling the fixture since it is returning the driver
  login_page=LoginPage(driver)
  driver.get(pass_Url)
  print(login_page.getTitle())
  shop_Page=login_page.login(test_list_items["username"],test_list_items["password"])
  print(shop_Page.getTitle())
  shop_Page.AddToCart(test_list_items["productname"]) #passing prd_name as an argument

  chckout_page=shop_Page.checkout() #calling the checkout page object in shop page
  print(chckout_page.getTitle())
  chckout_page.chckOut_Confirm()
  chckout_page.location_select("India")
  chckout_page.confirmation_msge()









