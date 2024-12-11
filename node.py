class Node:
    _node_memory = []
    
    def __init__(self, title:str, link:str, depth:int, last_node:object):
        self.title = title
        self.link = link
        self.depth = depth #warstwa na ktorej jest dany node
        self.parent_node = last_node 
        Node._node_memory.append(self)

    def __str__(self) -> str:
        return f"Nazwa: {self.title}, Warstwa/glebokosc: {self.depth}"
    
    @staticmethod
    def sort_memory_by_depth(depth:int) -> list: #returns an array of nodes with correct depth
        return_array = []
        for i in Node._node_memory:
            if i.depth == depth:
                return_array.append(i)
        return return_array

    @staticmethod
    def get_highest_depth() -> int:
        high = 0
        for i in Node._node_memory:
            if i.depth > high:
                high = i.depth
        return high

    @classmethod #Used to wipe internal storage of node class
    def node_memory_wipe():
        Node._node_memory = []
    
    @staticmethod
    def print_out_whole_tree(): #prints out hole tree
        for i in range(Node.get_highest_depth() + 1):
            for j in Node.sort_memory_by_depth(i):
                print(f"{i} \n {j.title}")
        
    

"""
    UWAGI:
        BRAK
"""
