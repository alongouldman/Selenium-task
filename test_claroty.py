import unittest
from selenium import webdriver
from pages import *


class TestClaroty(unittest.TestCase):
    """
    a unittest class to test the claroty website.
    The tests by this class are:
    1. Go to google.com
    2. Search 'Claroty'
    3. Print to console the results number
    4. Make sure that claroty.com is the first result's link
    5. Go to https://www.claroty.com/careers
    6. Print to console the number of carriers
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)  # sets the maximum number of time to wait for selenium

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.driver.delete_all_cookies()  # in order to make every test independent

    def test_number_of_results(self):
        """
        Prints to console the results number
        """
        google = Google(self.driver)
        google.search("Claroty")
        search_results_page = GoogleSearchResults(self.driver)
        num = search_results_page.get_number_of_results()
        print(f"Number of search results for Claroty in Google (estimated): {num}")

    def test_claroty_is_first(self):
        """
        Make sure that claroty.com is the first result's link
        """
        CLAROTY_URL = "https://www.claroty.com"  # this url needs to be first
        google = Google(self.driver)
        google.search("Claroty")
        search_results_page = GoogleSearchResults(self.driver)
        self.assertTrue(url_domain_compare(search_results_page.get_first_result_link(), CLAROTY_URL))

    def test_claroty_careers(self):
        # 5. Go to https://www.claroty.com/careers
        claroty_careers = ClarotyCareers(self.driver)

        # 6. Print to console the number of carriers
        num_of_careers = claroty_careers.number_of_careers()
        print(f"Open careers in Claroty: {num_of_careers}")


if __name__ == "__main__":
    unittest.main()
