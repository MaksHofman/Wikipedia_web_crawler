from bs4 import BeautifulSoup
import requests
import node
import multiprocessing 

class Scraper:
    _wikipedia_base_link = "https://wikipedia.org/" #link do wikipedi !!!mozna dodac kraj jako zmiena zeby informacje byly w jezyku zachcianym
    _max_depth = 15

    def __init__(self, web_page_name:str, depth:int):
        self.web_page_name = web_page_name
        self.depth = depth
        
        re = requests.get(self.web_page_name)
        root_soup = BeautifulSoup(re.text, features="lxml")
        root_node = node(Scraper.html_into_node_init(root_soup),web_page_name, 0) # incjializacja root noda
        for link in root_soup.find_all('a'): # 1 loop
            Scraper.scrape_single_link(link.get('href'), 0, root_node)

    #make it multiprocesing able
    def scrape_single_link(Link: str, depth:int, last_node:node):
        
        re = requests.get(Link)
        child_soup = BeautifulSoup(re.text, features="lxml")
        child_node = node(Scraper.html_into_node_init(child_soup), link, depth+1, last_node) #init child node
        for link in child_soup.find_all('a'):
            Scraper.scrape_single_link(link.get('href'), depth+1, child_node) #repet proces
    
    def html_into_title(soup):
        return soup.title.text



#test code HERE
if __name__ == "__main__":
    wikipedia_test = "https://pl.wikipedia.org/wiki/Operacja_Harekate_Yolo"
    re = requests.get(wikipedia_test)
    print(re.status_code)
    soup = BeautifulSoup(re.text, features="lxml")
    for link in soup.find_all('a'):
        print(link.get('href'))

    """
    Trzeba przemyslec jak incjializujemy scraping. Myslalem zeby w konstruktorze rozpoczac tak ze juz wywolany scraper ma wszystkie dane.
    + mozna zrobic jakas kolase do analizy i wizualizacj tych danych zeby bylo tak fancy
    """