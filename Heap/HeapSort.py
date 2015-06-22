__author__ = 'Andrea'


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

    @classmethod
    def heapsort_inplace(cls, heap):

        length = len(heap.heap)

        while length > 0:

            node_to_delete = heap.heap[0]
            node_leaf = heap.heap[length - 1]
            heap.swap_node(node_to_delete, node_leaf)
            heap.move_down(node_leaf)

            length -= 1

        return heap.heap
