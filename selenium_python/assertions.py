import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from helpers import EXECUTION_LINK

class AssertionsTest(unittest.TestCase):
    #Lunch browser
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(EXECUTION_LINK)
        driver.implicitly_wait(10)

    #Assertions TEST_1
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME,'q'))
    
    #Assertions TEST_2
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, "select-language"))

    #Function to check is a element is present
    def is_element_present(self, how, what):
        #(try) is used to catch a exception, in which if:
        #Is catched, that means the search of a element (by=how, By.NAME) and (value=what, 'q') returned nothing
        #Is not catched, that means the search of the element was successful
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True

    #Close browser
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)