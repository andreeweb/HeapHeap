
class BinomialHeapNode:
    
    def __init__(self, elem, key):
        self.elem = elem
        self.key = key
        self.father = None
        self.children = []

    def add_son(self, son):
        son.father = self
        self.children.append(son)
