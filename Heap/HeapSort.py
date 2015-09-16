

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
                ordered_array.append(min_node)
        return ordered_array
