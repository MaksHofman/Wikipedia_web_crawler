class Node:
    _node_memory = []
    __last_node = None
    def __init__(self, title, link, depth):
        self.title = title
        self.link = link
        self.depth = depth
        self.parent_node = Node.__last_node #to trzeba zmienic
        Node._node_memory.append(self)

    @classmethod #Used to wipe internal storage of node class
    def node_memory_wipe():
        Node._node_memory = []
        Node.__last_node = None

        """
        Trzeba przemyslec te __last_node moim zdaniem. Trzeba zrobic tak zeby dalo sie elegancko uzyc multiprocesing. wiec trzeba do tego strukture przygotowac(node)
        Chyba parent node bedzie trzeba zrobic jako zmiena podana od scrapera inczej nie pujdzie
        """