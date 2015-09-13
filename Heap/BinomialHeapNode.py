
class BinomialHeapNode:
    
    def __init__(self, elem, key):
        self.elem = elem
        self.key = key
        self.father = None
        self.sons = []

    def add_son(self, son):
        son.father = self
        self.sons.append(son)

    def swap_node(self, other_node):
        self.elem, other_node.elem = other_node.elem, self.elem
        self.key, other_node.key = other_node.key, self.key


