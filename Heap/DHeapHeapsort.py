
from Heap.DHeapQueue import DHeapQueue
from Heap.DHeapNode import DHeapNode


class DHeapHeapsort(DHeapQueue):

    def __init__(self, heap, d):
        super().__init__(d)
        self.length = len(heap.heap)

    def get_min_son(self, node):
        # Son law: d*(index)+{1,...,d}
        count = 1
        min_son = DHeapNode(None, float('inf'), None)
        while count <= self.d:
            son_index = (self.d*node.index)+count
            if son_index >= self.length:
                break
            son = self.heap[son_index]
            if son.key < min_son.key:
                min_son = son
            count += 1
        return min_son

    def delete_min(self):
        if self.length == 0:
            return
        first = self.heap[0]
        last = self.heap[self.length - 1]
        self.swap_node(first, last)
        self.length -= 1
        self.move_down(last)

    def is_empty(self):
        if self.length == 0:
            return True
        return False
