__author__ = 'Andrea'

from HeapNode import HeapNode

class DHeap:

    def __init__(self, d):
        self.d = d
        self.heap = []

    def get_min(self):
        if not self.is_empty():
            return self.heap[0]
        else:
            return None

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False

    def delete(self, node):
        if len(self.heap) == 0:
            return
        node_to_delete = self.heap[node.index]
        node_leaf = self.heap[- 1]
        self.swap_node(node_to_delete, node_leaf)
        del self.heap[-1]
        self.move_up(node_leaf)
        self.move_down(node_leaf)

    def insert(self, elem, key):
        new_node = HeapNode(elem, key, len(self.heap))
        self.heap.append(new_node)
        self.move_up(new_node)

    def get_min_son(self, node):
        # Son law: d*(index)+{1,...,d}
        count = self.d
        min_son = None
        while count > 0:
            son = self.heap[(self.d*node.index)+count]
            if min_son < son:
                min_son = son
            count -= 1
        return min_son

    def move_down(self, node):
        min_son = self.get_min_son(node)
        if min_son is None or node.key <= min_son.key:
            return
        else:
            self.swap_node(node, min_son)

    def move_up(self, node):
        if node.index == 0:
            return
        father = self.heap[(node.index - 1) / self.d]
        while self.get_min() is not None and node.key < father.key:
            self.swap_node(node, father)

    def swap_node(self, node_1, node_2):
        self.heap[node_1.index], node_1.index = node_2, node_2.index
        self.heap[node_2.index], node_2.index = node_1, node_1.index

    def print_heap(self):
        s = ""
        for i in range(len(self.heap)):
            n = self.heap[i]
            s += "[{},{}] ".format(n.elem, n.key)
        print(s)
