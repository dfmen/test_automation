import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from helpers import EXECUTION_LINK

class HelloWorld(unittest.TestCase):
    #Initializing webdriver as driver
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #Lunch browser
    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    #Open web_page
    def test_hello_world(self):
        self.driver.get(EXECUTION_LINK)

    #Click button "Ingresar"
    def test_login(self):
        button_login = self.driver.find_element(By.XPATH, '//*[@id="Header-v2"]/nav/div[5]/div/a')
        button_login.click()
    
    #Close browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='REPORTS', report_name='hello-world-REPORT'))