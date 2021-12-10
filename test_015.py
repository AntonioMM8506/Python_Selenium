import unittest
from selenium import webdriver
#from selenium.webdriver.common.by import By 
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#Sorting tables
#Sortable Data Tables

class Typos(unittest.TestCase):

    #Initialization
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/ASUS/Documents/VS Code/JavaScript/Platzi/Selenium/chromedriver.exe')
        driver= self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Sortable Data Tables").click()

    #Test Cases
    #This case checks if the given text is equal to the one corresponding to the web page. 
    def test_sort_tables(self):
        driver = self.driver

        #Fills the list with other lists
        table_data = [[] for i in range(5)]
        print(table_data)

        #Find the elements of the header from the table by its xpath. 
        for i in range(5):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i+1}]/span')
            table_data[i].append(header.text)

            for j in range(4):
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
                table_data[i].append(row_data.text)

        print(table_data)

    #Close
    def tearDown(self):
        self.driver.close()


#MAIN
if __name__== '__main__':
    unittest.main(verbosity=2)