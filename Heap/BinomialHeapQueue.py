__author__ = 'Andrea'

from Heap.BinomialHeap import BinomialHeap

class BinomialHeapQueue:

    def __init__(self, size):
        self.heap = size * [None]
        self.size = size

    def is_empty(self):
        print(self.heap)
        return None

    def find_min(self):

        if self.is_empty():
            return None

        min_root = float('inf')

        for i in range(self.size):
            if self.heap[i] < min_root:
                min_root = self.heap[i]
        return min_root

    # Si aggiunge un B0, e poi si ristruttura
    def insert(self, e, k):
        nHeap = BinomialHeap(e, k)
        root = nHeap.root
        if self.heap[0][0] == None:
            self.heap[0][0] = nHeap
        else:
            self.heap[0][1] = nHeap
            self.rebuild()
        return root

    def insert(self, elem, key):

        # create a new B0
        new_heap_b0 = BinomialHeap(elem, key)
