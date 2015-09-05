
import time

from Heap.HeapSort import HeapSort
from Heap.DHeapQueue import DHeap

if __name__ == "__main__":

    start = time.time()

    pq = DHeap(4)

    if pq.is_empty():
        print("Empty")

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

    print("\n\n")

    print(HeapSort.heapsort_inplace(pq))
    # print(HeapSort.heapsort_support(pq))
