import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

class HelloWorld(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='C:/py/py_Selenium/venvPy/Include/chromedriver.exe')
        driver=cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver=self.driver
        driver.get('https://www.platzi.com')

    def test_login(self):
        driver = self.driver
        button_login = driver.find_element(By.XPATH, '//*[@id="Header-v2"]/nav/div[5]/div/a')
        button_login.click()
        
    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='REPORTS', report_name='hello-world-REPORT'))