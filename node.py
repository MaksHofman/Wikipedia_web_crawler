class Node:
    _node_memory = []
    
    def __init__(self, title, link, depth, last_node):
        self.title = title
        self.link = link
        self.depth = depth
        self.parent_node = last_node #to trzeba zmienic
        Node._node_memory.append(self)

    @classmethod #Used to wipe internal storage of node class
    def node_memory_wipe():
        Node._node_memory = []
        

        """
        Trzeba przemyslec te __last_node moim zdaniem. Trzeba zrobic tak zeby dalo sie elegancko uzyc multiprocesing. wiec trzeba do tego strukture przygotowac(node)
        Chyba parent node bedzie trzeba zrobic jako zmiena podana od scrapera inczej nie pujdzie
        """