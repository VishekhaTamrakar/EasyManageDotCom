import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class test2(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "maverick1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/accounts/login/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com")
       assert "Logged In"
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customerservice_list/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customerservice/new/")
       time.sleep(1)
       select = Select(driver.find_element_by_xpath("//*[@id='id_customer_name']"))
       select.select_by_index(2)
       select = Select(driver.find_element_by_xpath("//*[@id='id_service_category']"))
       select.select_by_index(2)
       driver.find_element_by_id("id_description").send_keys("Loaded Nachos")
       driver.find_element_by_id("id_service_charge").send_keys("12")
       time.sleep(1)
       driver.find_element_by_xpath("//*[@id='content']/form/button").click()
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customerservice_list/")




def tearDown(self):
       self.driver.close()
       time.sleep(1)

if __name__ == "__main__":
   unittest.main()