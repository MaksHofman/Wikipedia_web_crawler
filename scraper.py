from bs4 import BeautifulSoup
import requests

class Scraper:
    wikipedia_base_link = "https://wikipedia.org/" #link do wikipedi !!!mozna dodac kraj jako zmiena zeby informacje byly w jezyku zachcianym
    
    def __init__(self, web_page_name):
        self.web_page_name = web_page_name


if __name__ == "__main__":
    wikipedia_test = "https://pl.wikipedia.org/wiki/Operacja_Harekate_Yolo"
    re = requests.get(wikipedia_test)
    print(re.status_code)
    soup = BeautifulSoup(re.text, features="lxml")
    for link in soup.find_all('a'):
        print(link.get('href'))