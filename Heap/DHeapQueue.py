__author__ = 'Andrea'

from Heap.DHeapNode import HeapNode

class DHeap:

    def __init__(self, d):
        self.d = d
        self.heap = []

    def get_min(self):
        if not self.is_empty():
            return self.heap[0].elem
        else:
            return None

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False

    def delete(self, node):
        if len(self.heap) == 0:
            return None
        node_to_delete = self.heap[node.index]
        node_leaf = self.heap[- 1]
        self.swap_node(node_to_delete, node_leaf)
        del self.heap[-1]
        self.move_up(node_leaf)
        self.move_down(node_leaf)

    def delete_min(self):
        if len(self.heap) == 0:
            return None
        node_to_delete = self.heap[0]
        node_leaf = self.heap[- 1]
        self.swap_node(node_to_delete, node_leaf)
        del self.heap[-1]
        self.move_down(node_leaf)
        return node_to_delete

    def insert(self, elem, key):
        new_node = HeapNode(elem, key, len(self.heap))
        self.heap.append(new_node)
        self.move_up(new_node)

    def get_min_son(self, node):
        # Son law: d*(index)+{1,...,d}
        count = 1
        min_son = HeapNode(None, float('inf'), None)
        while count <= self.d:
            son_index = (self.d*node.index)+count
            if son_index >= len(self.heap):
                break
            son = self.heap[son_index]
            if son.key < min_son.key:
                min_son = son
            count += 1
        return min_son

    def move_down(self, node):
        while True:
            min_son = self.get_min_son(node)
            if min_son.elem is None or node.key <= min_son.key:
                break
            else:
                self.swap_node(node, min_son)

    def move_up(self, node):
        if node.index == 0:
            return
        father = self.heap[(node.index - 1) / self.d]
        while node.index > 0 and node.key < father.key:
            self.swap_node(node, father)

    def swap_node(self, node_1, node_2):
        self.heap[node_1.index] = node_2
        self.heap[node_2.index] = node_1
        node_1.index, node_2.index = node_2.index, node_1.index

    def print_heap(self):
        s = ""
        for i in range(len(self.heap)):
            n = self.heap[i]
            s += "[{} - {},{}] ".format(i, n.elem, n.key)
        print(s)
