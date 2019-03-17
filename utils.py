import re
from urllib.parse import urlparse


def extract_first_num(string_with_nums):
    """
    extracts the first number from a string.
    example: the string "About 462,000,000 results (0.38 seconds)"
    will output: " 462000000"
    :param string_with_nums: some string with numbers in it
    :return:
    """
    string_with_nums = string_with_nums.replace(',', "")  # to deal with comma separated numbers
    regex = r"(\d+)"
    num = re.search(regex, string_with_nums)
    return int(num.group())


def url_domain_compare(url1, url2):
    """
    compares two domains, ignoring lower/upper case, and subdomains etc.
    :param url1: first url to check
    :param url2: second url to check
    :return: true if it's the same domain, false otherwise
    """
    return urlparse(url1).netloc.lower() == urlparse(url2).netloc.lower()
