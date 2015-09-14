import time
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

if __name__ == "__main__":

    start = time.time()

    pq = BinomialHeapQueue(32)
    if pq.is_empty():
        print("Empty queue")

    e = 4.0
    k = 2.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()
    print("findMin():", pq.find_min())

    e = 2.0
    k = 1.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()
    print("findMin():", pq.find_min())

    e = 8.0
    k = 4.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()
    print("findMin():", pq.find_min())

    e = 10.0
    k = 5.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()
    print("findMin():", pq.find_min())

    e = 6.0
    k = 3.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()
    print("findMin():", pq.find_min())

    print("deleteMin()")
    pq.delete_min()
    pq.print_heap()
    print("findMin():", pq.find_min())

    e = 12.0
    k = 6.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    e = 14.0
    k = 7.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    e = 16.0
    k = 8.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)

    print("deleteMin()")
    pq.delete_min()
    pq.print_heap()

    e = 4.0
    k = 2.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    e = 2.0
    k = 1.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()

    end = time.time()
    print(str(end-start))
