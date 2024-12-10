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
        print("start_init")
        global threads 
        threads = list() #naprawic  puzniej trzeba to
        Scraper.scrape_single_link(link=self.web_page_name, depth=0, last_node=None, max_depth=depth)
        for thread in threads:
            thread.join()


    #make it multiprocesing able
    def scrape_single_link(link: str, depth:int, last_node:Node, max_depth = _max_depth):
        if depth == max_depth:
            return 
        req = requests.get(link)
        child_soup = BeautifulSoup(req.text, features="lxml")
        child_node = Node(title=child_soup.title.text, link=link, depth=depth, last_node=last_node) #init child node
        for i in child_soup.find_all('p'):
            for link in i.find_all('a'):
 
                if link.get('href') == None:
                    break
                if re.search("#.", str(link.get('href'))):
                    break

                #trzeba filtry nalozyc tu mozna tez duplikaty skipoowac
                duplicat_search_array = []
                
                if type( Scraper._wikipedia_base_link + link.get('href')) == str:
                    thread = threading.Thread(target=Scraper.scrape_single_link, args=(str(Scraper._wikipedia_base_link + link.get('href')), depth+1, child_node, max_depth))
                    threads.append(thread)
                    thread.start()

    """@classmethod        
    def html_into_title(soup:object) -> str:   chyba  usess funkcjia
        return str(soup.title.text)"""



#test code HERE
if __name__ == "__main__":
    #Trzeba napisac testy do calej klasy
    New_scrap = Scraper("https://pl.wikipedia.org/wiki/Grupa_Fortowa_%E2%80%9ECarski_Dar%E2%80%9D_Twierdzy_Modlin", 2)
    Node.print_out_whole_tree()
    print("koniec")


    """
    UWAGI:
    Threading jeszce niedziala. Chyba filtr jest dobry (trzeba tez chyba fundation wywalac). Output sie nie generuje poprawnie
    """