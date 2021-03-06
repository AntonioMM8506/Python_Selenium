#Explicit Wait
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from selenium import webdriver
#from selenium.webdriver.common.by import BY 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExplicitWaitTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
        self.driver.get("http://demo-store.seleniumacademy.com")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
    #End of setUp


    def test_acount_link(self):
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id("select-language").get_attribute("length") == "3")
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "ACCOUNT")))
        account.click()
    #End of test_acount_link

    def test_create_new_customer(self):
        self.driver.find_element_by_link_text("ACCOUNT").click()
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "My Account")))
        my_account.click()

        create_account_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "CREATE AN ACCOUNT")))
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains("Create New Customer Account"))
    #End of test_create_new_customer

    def tearDown(self):
        self.driver.close()
    #End of tearDown

#MAIN    
if __name__ == "__main__":
	unittest.main(verbosity = 2)
