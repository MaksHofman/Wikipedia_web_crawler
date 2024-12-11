from bs4 import BeautifulSoup
import requests
from node import Node
import threading
import re
class Scraper:
    _jezyk_polski = "pl."
    _wikipedia_base_link = f"https://{_jezyk_polski}wikipedia.org/" #link do wikipedi !!!mozna dodac kraj jako zmiena zeby informacje byly w jezyku zachcianym
    _max_depth = 5

    def __init__(self, web_page_name:str, depth:int):
        self.web_page_name = web_page_name
        self.depth = depth
        print("start_init")
        unwanted_array = []
        global threads  #trzxeba to naprawic (nw jak)
        threads = list() 
        Scraper.scrape_single_link(link=self.web_page_name, depth=0, last_node=None, max_depth=depth, unwanted_array=unwanted_array)
        for thread in threads:
            thread.join()

    #make it multiprocesing able
    def scrape_single_link(link: str, depth:int, last_node:Node, max_depth = _max_depth, unwanted_array = []): #?
        if depth > max_depth:
            return 
        req = requests.get(link)
        child_soup = BeautifulSoup(req.text, features="lxml")
        #filtry zeby bledne nody sie nie tworzyly
        if ("Not Found"  or "") == str(child_soup.title.text):
            return
        if re.search("Plik:.", str(child_soup.title.text)) or re.search("File:.", str(child_soup.title.text)) or re.search("Szablon:.", str(child_soup.title.text)) or re.search("Dyskusja szablonu:.", str(child_soup.title.text))or re.search("Wikipedia:.", str(child_soup.title.text)) or re.search("Pomoc:.", str(child_soup.title.text)) or re.search("Edytujesz.", str(child_soup.title.text)):
            return
        
        child_node = Node(title=child_soup.title.text, link=link, depth=depth, last_node=last_node) #init child node
        for i in child_soup.find_all(id="bodyContent"):
            for link in i.find_all('a'):
 
                if link.get('href') == None:
                    break
                if re.search("#.", str(link.get('href'))):
                    break
                
                #Trzeba zrobic filtry dla tych tablic
                if Scraper.search_if_is_in_array(str(link.get('href')), unwanted_array):
                    break
                
                else:
                    unwanted_array.append(link.get('href'))
                 #doniej trzeba dodac duplikaty i niechciane elementy
            
                
                if type( Scraper._wikipedia_base_link + link.get('href')) == str:# ten if chyba nie potrzebny
                    thread = threading.Thread(target=Scraper.scrape_single_link, args=(str(Scraper._wikipedia_base_link + link.get('href')), depth+1, child_node, max_depth))
                    threads.append(thread)
                    thread.start()
   
    @staticmethod
    def search_if_is_in_array(input:str, array:list) -> bool: #sus list ale nw jak to zapisac normalnie
        for i in array:
            if input == i:
                return True
        return False
    
#test code HERE
if __name__ == "__main__":
    #Trzeba napisac testy do calej klasy
    New_scrap = Scraper("https://pl.wikipedia.org/wiki/Grupa_Fortowa_%E2%80%9ECarski_Dar%E2%80%9D_Twierdzy_Modlin", 2)
    Node.print_out_whole_tree()
    for i in Node._node_memory:
        print(str(i))
    print("koniec")


    """
    UWAGI:
    Threading dziala. Trzeba poprawic filtry i duplikaty
    DO ZROBIENIA:
    1. Filtry dodac
    2. Upiekrzyc kod
    3. Jakas klasa do analizy lub dodac szukania specjalnego linka w drzewku.
    4. moze jakas wizualizacja
    """