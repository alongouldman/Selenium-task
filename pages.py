from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import *


class BasePage:
    """
    This is the base page object of Page Object Model (POM)
    """
    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        """
        goes to the url of the page
        :param url: url to go to
        """
        self.driver.get(url)


class Google(BasePage):

    GOOGLE_URL = "https://www.google.com/"
    SEARCH_BAR = (By.NAME, 'q')

    def __init__(self, driver):
        super().__init__(driver)  # init base page
        super().go_to(self.GOOGLE_URL)  # goes to google

    def search(self, query):
        # 2. Search 'Claroty'
        elem = self.driver.find_element(*self.SEARCH_BAR)
        elem.send_keys(query)
        elem.send_keys(Keys.RETURN)


class GoogleSearchResults(BasePage):

    SEARCH_RESULTS = (By.ID, 'resultStats')
    MAIN_SEARCH_RESULTS = (By.CSS_SELECTOR, "#center_col #search")
    FIRST_LINK = (By.TAG_NAME, 'link')

    def get_first_result_link(self):
        """
        :return: the link of the first result in google of this search results page.
        note: not including paid search results!
        """
        search_page = self.driver.find_element(*self.MAIN_SEARCH_RESULTS)  # make sure it's not the paid search
        return search_page.find_element(*self.FIRST_LINK).get_attribute('href')

    def get_number_of_results(self):
        """
        returns an approximate number of search results from google
        :return: the number of search results
        """
        num_of_results = self.driver.find_element(*self.SEARCH_RESULTS)
        num = extract_first_num(num_of_results.text)  # gets the first number from the result
        return int(num)


class ClarotyCareers(BasePage):

    CLAROTY_CAREERS_URL = "https://www.claroty.com/careers"
    SINGLE_CAREER = (By.CSS_SELECTOR, ".w-dyn-items .w-dyn-item")

    def __init__(self, driver):
        super().__init__(driver)
        super().go_to(self.CLAROTY_CAREERS_URL)

    def number_of_careers(self):
        """
        returns the number of careers on claroty's website
        :return:
        """
        careers = self.driver.find_elements(*self.SINGLE_CAREER)
        return len(careers)
