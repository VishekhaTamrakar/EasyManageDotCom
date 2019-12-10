import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/about/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       time.sleep(1)
       driver.find_element_by_xpath("//*[@id='content']/table/tbody/tr[2]/td[12]/a").click()
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer/1/edit/")
       time.sleep(1)
       driver.find_element_by_id("id_zipcode").clear()
       driver.find_element_by_id("id_zipcode").send_keys("68122")
       time.sleep(2)
       driver.find_element_by_xpath("//*[@id='content']/div/form/button").click()
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer/new/")
       elem = driver.find_element_by_id("id_customer_id")
       elem.send_keys("12")
       elem = driver.find_element_by_id("id_customer_name")
       elem.send_keys("Nancy")
       elem = driver.find_element_by_id("id_city")
       elem.send_keys("Omaha")
       elem = driver.find_element_by_id("id_state")
       elem.send_keys("NE")
       elem = driver.find_element_by_id("id_zipcode")
       elem.send_keys("68127")
       elem = driver.find_element_by_id("id_contact_details")
       elem.send_keys("4029959072")
       elem = driver.find_element_by_id("id_email_address")
       elem.send_keys("nancy_jain@yhaoo.com")
       elem = driver.find_element_by_id("id_customer_room_no")
       elem.send_keys("126")
       elem = driver.find_element_by_id("id_customer_stay_start_date")
       elem.send_keys()
       elem = driver.find_element_by_id("id_customer_stay_end_date")
       elem.send_keys()
       elem = driver.find_element_by_xpath("//*[@id='content']/form/button")
       elem.click()
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer/12/delete")
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       time.sleep(1)

def tearDown(self):
       self.driver.close()
       time.sleep(1)

if __name__ == "__main__":
   unittest.main()


