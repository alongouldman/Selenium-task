import re
from urllib.parse import urlparse


def extract_num(string_with_nums):
    string_with_nums = string_with_nums.replace(',', "")
    regex = r"(\d+)"
    num = re.search(regex, string_with_nums)
    return num.group()


def url_domain_compare(url1, url2):
    return urlparse(url1).netloc.lower() == urlparse(url2).netloc.lower()


if __name__ == "__main__":
    print(url_domain_compare('https://www.claroty.com', 'http://www.Claroty.com/careers'))