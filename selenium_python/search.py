import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers import EXECUTION_LINK

class SearchTest(unittest.TestCase):
    #Lunch browser
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(EXECUTION_LINK)
        driver.implicitly_wait(10)

    #Search TEST_1
    def test_search_tee(self):
        search_field = self.driver.find_element(By.NAME,'q')
        search_field.clear()

        search_field.send_keys("tee")
        search_field.submit()
    
    #Search TEST_2
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()

        search_field.send_keys("salt shaker")
        search_field.submit()

        products = driver.find_elements(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))

    #Close browser
    def tearDown(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)