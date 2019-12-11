import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test2(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "arvind"
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
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/about/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       time.sleep(2)
       driver.find_element_by_xpath("//*[@id='content']/table/tbody/tr[2]/td[10]/a").click()
       time.sleep(2)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customerservice_list/")
       time.sleep(2)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/roomstatus_list/")
       time.sleep(2)
       driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[2]").click()
       time.sleep(2)

   def tearDown(self):
       self.driver.close()
       time.sleep(10)

if __name__ == "__main__":
   unittest.main()