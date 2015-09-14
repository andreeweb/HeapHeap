import time
from Heap.BinaryHeapNode import BinaryHeapNode
from Heap.DHeapQueue import DHeapQueue
import math


class BinaryHeapQueue(DHeapQueue):

    def __init__(self):
        super().__init__(2)

    def get_min_son(self, node):
        count = 1
        min_son = BinaryHeapNode(None, float('inf'), None)
        while count <= 2:
            son_index = (2*node.index)+count
            if son_index >= len(self.heap):
                break
            son = self.heap[son_index]
            if son.key < min_son.key:
                min_son = son
            count += 1
        return min_son

    def move_up(self, son):
        if son.index <= 0:
            return
        father = self.heap[math.trunc((son.index - 1) / 2)]
        while son.index > 0 and son.key < father.key:
            self.swap_node(son, father)
            father = self.heap[math.trunc((son.index - 1) / 2)]

    def move_down(self, father):
        son = self.get_min_son(father)
        while son is not None and son.key < father.key:
            self.swap_node(father, son)
            son = self.get_min_son(father)

    def insert(self, elem, key):
        new_node = BinaryHeapNode(elem, key, len(self.heap))
        self.heap.append(new_node)
        self.move_up(new_node)

if __name__ == "__main__":

    start = time.time()

    pq = BinaryHeapQueue()
    if pq.is_empty():
        print("Empty queue")

    e = 4.0
    k = 2.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()
    print("findMin():", pq.get_min())

    e = 2.0
    k = 1.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()
    print("findMin():", pq.get_min())

    e = 8.0
    k = 4.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()
    print("findMin():", pq.get_min())

    e = 10.0
    k = 5.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()
    print("findMin():", pq.get_min())

    e = 6.0
    k = 3.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()
    print("findMin():", pq.get_min())

    print("deleteMin()")
    pq.delete_min()
    pq.print_heap()
    print("findMin():", pq.get_min())

    e = 12.0
    k = 6.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()

    e = 14.0
    k = 7.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()

    e = 16.0
    k = 8.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.print_heap()

    print("deleteMin()")
    pq.delete_min()
    pq.print_heap()

    end = time.time()
    print(str(end-start))
