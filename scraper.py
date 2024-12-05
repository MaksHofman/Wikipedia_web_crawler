from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, web_page_name):
        self.web_page_name = web_page_name


if __name__ == "__main__":
    wikipedia_test = "https://pl.wikipedia.org/wiki/Operacja_Harekate_Yolo"
    re = requests.get(wikipedia_test)
    print(re.status_code)
    soup = BeautifulSoup(re.text)
    print(soup.prettify())