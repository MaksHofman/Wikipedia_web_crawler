from bs4 import BeautifulSoup
import requests
from node import Node
import threading
import re
class Scraper:
    _wikipedia_base_link = "https://wikipedia.org/" #link do wikipedi !!!mozna dodac kraj jako zmiena zeby informacje byly w jezyku zachcianym
    _max_depth = 2

    def __init__(self, web_page_name:str, depth:int):
        self.web_page_name = web_page_name
        self.depth = depth
        Scraper.scrape_single_link(link=self.web_page_name, depth=-1, last_node=None, max_depth=depth)


    #make it multiprocesing able
    def scrape_single_link(link: str, depth:int, last_node:Node, max_depth = _max_depth):
        if depth == max_depth:
            return
        re = requests.get(link)
        child_soup = BeautifulSoup(re.text, features="lxml")
        child_node = Node(title=child_soup.title.text, link=link, depth=depth+1, last_node=last_node) #init child node
        for i in child_soup.find_all('p'):
            for link in i.find_all('a'):
            #tutaj trzeba dodac multiprocesing
                #print(link.get('href'))
                if re.search("#.", link.get('href').text):
                    pass
                #trzeba filtry nalozyc tu mozna tez duplikaty skipoowac
                duplicat_search_array = []
                
                if link.get('href') == None:
                    pass
                if type( Scraper._wikipedia_base_link + link.get('href')) == str:
                    thread = threading.Thread(target=Scraper.scrape_single_link, args=(str(Scraper._wikipedia_base_link + link.get('href')), depth+1, child_node, max_depth))
                    thread.start()

    @classmethod        
    def html_into_title(soup:object) -> str:
        return str(soup.title.text)



#test code HERE
if __name__ == "__main__":
    #Trzeba napisac testy do calej klasy
    New_scrap = Scraper("https://pl.wikipedia.org/wiki/Operacja_Harekate_Yolo", 2)
    Node.print_out_whole_tree


    """
    #stary kod
    wikipedia_test = "https://pl.wikipedia.org/wiki/Operacja_Harekate_Yolo"
    re = requests.get(wikipedia_test)
    print(re.status_code)
    soup = BeautifulSoup(re.text, features="lxml")
    for link in soup.find_all('a'):
        print(link.get('href'))

    Trzeba przemyslec jak incjializujemy scraping. Myslalem zeby w konstruktorze rozpoczac tak ze juz wywolany scraper ma wszystkie dane.
    + mozna zrobic jakas kolase do analizy i wizualizacj tych danych zeby bylo tak fancy
    """