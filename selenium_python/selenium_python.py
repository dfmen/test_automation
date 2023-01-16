import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers import EXECUTION_LINK

class HelloWorld(unittest.TestCase):
    #Lunch browser
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get(EXECUTION_LINK)
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    #Open web_page
    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID, "search")
    
    #Test 1
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element(By.NAME, "q") 

    #Test 1
    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "input-text") 

    #Test, to check if a button is enable
    def test_search_button_enable(self):
        button = self.driver.find_element(By.CLASS_NAME, "button")
        button.is_enabled()

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
        banners = banner_list.find_elements(By.TAG_NAME, 'img')
        self.assertEqual(3, len(banners))

    def test_if_banners_equals_to_three(self):
        banners = self.driver.find_elements(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/ul')

    def test_shopping_cart(self):
        shopping_cart = self.driver.find_element(By.CSS_SELECTOR, "div.header-minicart span.icon")

    #Close browser
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)