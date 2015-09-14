

class DHeapNode:

    def __init__(self, elem, key, index):
        self.elem = elem
        self.key = key
        self.index = index

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)
