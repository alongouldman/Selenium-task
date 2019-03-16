import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utils import *


def get_num_of_results(element):
    elememt_text = element.text
    children_text = 0


class TestClaroty(unittest.TestCase):

    GOOGLE_URL = "https://www.google.com/"
    CLAROTY_URL = "https://www.claroty.com"
    CLAROTY_CAREERS_URL = "https://www.claroty.com/careers"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        # pass

    def setUp(self):
        self.driver.delete_all_cookies()

    def search_google(self):
        #  1. Go to google.com
        self.driver.get(self.GOOGLE_URL)

        # 2. Search 'Claroty'
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("Claroty")
        elem.send_keys(Keys.RETURN)

    def test_number_of_results(self):
        """
        Prints to console the results number
        """
        self.search_google()
        num_of_results = self.driver.find_element_by_id('resultStats')
        children = num_of_results.find_element_by_tag_name('nobr')
        num = num_of_results.text.replace(children.text, '')
        num = extract_num(num)
        print(f"Number of search results for Claroty in Google (estimated): {num}")

    def test_claroty_is_first(self):
        """
        Make sure that claroty.com is the first result's link
        """
        self.search_google()
        search_page = self.driver.find_element_by_css_selector("#center_col #search")
        first_link = search_page.find_element_by_tag_name('link').get_attribute('href')
        self.assertTrue(url_domain_compare(first_link, self.CLAROTY_URL))

    def test_claroty_careers(self):
        # 5. Go to https://www.claroty.com/careers
        driver = self.driver
        driver.get(self.CLAROTY_CAREERS_URL)

        # 6. Print to console the number of carriers
        careers = driver.find_elements_by_css_selector(".w-dyn-items .w-dyn-item")
        print(f"Open careers in Claroty: {len(careers)}")


if __name__ == "__main__":
    unittest.main()
