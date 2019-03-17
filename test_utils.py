import unittest
from utils import *


@unittest.skip("internal tests")
class TestUrlsCompare(unittest.TestCase):
    """
    Internal tests for my utils functions
    """
    SUB = "www"
    DOMAIN = "google"
    PROTOCOL1 = "https://"
    PROTOCOL2 = "http://"
    TLD1 = "com"
    TLD2 = "co.il"
    PARAMS = r"/search?ei=azmOXJPUEoTbwQK91KOICg"
    URL = f"{PROTOCOL1}{SUB}.{DOMAIN}.{TLD1}"

    def test_protocol(self):
        other_url = f"{self.PROTOCOL2}{self.SUB}.{self.DOMAIN}.{self.TLD1}"
        self.assertTrue(url_domain_compare(other_url, self.URL))

    def test_upper_case(self):
        other_url = f"{self.PROTOCOL1}{self.SUB}.{self.DOMAIN.upper()}.{self.TLD1}"
        self.assertTrue(url_domain_compare(other_url, self.URL))

    def test_tld(self):
        other_url = f"{self.PROTOCOL1}{self.SUB}.{self.DOMAIN}.{self.TLD2}"
        self.assertFalse(url_domain_compare(other_url, self.URL))  # google.com and google.co.il are not the same site

    def test_parameters(self):
        other_url = f"{self.PROTOCOL1}{self.SUB}.{self.DOMAIN}.{self.TLD1}{self.PARAMS}"
        self.assertTrue(url_domain_compare(other_url, self.URL))


class TestExtractFirstNum(unittest.TestCase):

    NUMBER = 123456
    TEXT = "some text here"

    def test_number_beggining(self):
        text = f"{self.NUMBER} {self.TEXT}"
        self.assertEqual(self.NUMBER, extract_first_num(text))

    def test_number_end(self):
        text = f"{self.TEXT} {self.NUMBER}"
        self.assertEqual(self.NUMBER, extract_first_num(text))

    def test_number_between(self):
        text = f"{self.TEXT} {self.NUMBER} {self.TEXT}"
        self.assertEqual(self.NUMBER, extract_first_num(text))

    def test_number_tite(self):
        text = f"{self.TEXT}{self.NUMBER}{self.TEXT}"
        self.assertEqual(self.NUMBER, extract_first_num(text))

    def test_two_numbers(self):
        text = f"{self.NUMBER} {self.NUMBER}"
        self.assertEqual(self.NUMBER, extract_first_num(text))

    def test_commas(self):
        comma_seperated = ",".join(list(str(self.NUMBER)))
        text = f"{comma_seperated}"
        self.assertEqual(self.NUMBER, extract_first_num(text))


if __name__ == "__main__":
    unittest.main()
