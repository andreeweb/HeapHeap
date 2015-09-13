
from Heap.BinomialHeap import BinomialHeap


class BinomialHeapQueue:

    def __init__(self, max_size):
        self.heap = max_size * [[None, None, None]]
        self.max_size = max_size

    def rebuild(self):

        for i in range(len(self.heap)):
            if self.heap[i][1] is None and self.heap[i][2] is None:
                continue

            if self.heap[i][1] is not None and self.heap[i][2] is not None:
                merged = self.heap[i][1].merge(self.heap[i][2])
                self.heap[i][1] = self.heap[i][2] = None
            else:
                merged = self.heap[i][0].merge(self.heap[i][1])
                self.heap[i][0] = self.heap[i][1] = None

            if self.heap[i + 1][0] is None:
                self.heap[i + 1][0] = merged
            elif self.heap[i + 1][1] is None:
                self.heap[i + 1][1] = merged
            else:
                self.heap[i + 1][2] = merged

    def is_empty(self):
        for i in range(len(self.heap)):
            if self.heap[i][0] is not None:
                return False
        return True

    def insert(self, e, k):
        new_heap = BinomialHeap(e, k)
        root = new_heap.root
        if self.heap[0][0] is None:
            self.heap[0][0] = new_heap
        else:
            self.heap[0][1] = new_heap
            self.rebuild()
        return root

    def find_min_index(self):
        if self.is_empty():
            return -1
        for best in range(self.max_size):
            if self.heap[best][0] is not None:
                break
        for i in range(best + 1, self.max_size):
            if self.heap[i][0] is not None and self.heap[i][0].root.key < self.heap[best][0].root.key:
                best = i
        return best

    def find_min(self):
        if self.is_empty():
            return None
        return self.heap[self.find_min_index()][0].root.elem

    def delete_min(self):
        if self.is_empty():
            return
        index = self.find_min_index()
        new = self.heap[index][0].get_heap_sons()
        self.heap[index][0] = None
        count = 0
        length = len(new)
        while length > 0:
            current = new[count]
            if self.heap[count][0] is None:
                self.heap[count][0] = current
            else:
                self.heap[count][1] = current
            count += 1
            length -= 1
        self.rebuild()

    def print_heap(self):
        self.heap[0][0].print_heap()
