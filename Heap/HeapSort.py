
from Heap import DHeapHeapsort


class HeapSort:

    @classmethod
    def heapsort_support(cls, heap):

        # create support array
        ordered_array = []

        # extract min until heap is empty
        while not heap.is_empty():
            min_node = heap.delete_min()
            if min_node is None:
                break
            else:
                ordered_array.insert(0, min_node)

        return ordered_array

    @classmethod
    def heapsort_inplace(cls, heap):

        if not isinstance(type(heap), DHeapHeapsort):
            raise AssertionError('heapsort_inplace only works on DHeapHeapsort queue')

        while not heap.is_empty():
            heap.delete_min()

        return heap.heap
