from Heap.BinomialHeapNode import BinomialHeapNode


class BinomialHeap:

    def __init__(self, elem, key):
        self.root = BinomialHeapNode(elem, key)

    def merge(self, heap_to_merge):

        this_root = self.root
        to_merge_root = heap_to_merge.root

        if this_root.key <= to_merge_root.key:
            heap_to_merge.father = this_root
            this_root.add_son(to_merge_root)
            return self
        else:
            this_root.father = to_merge_root
            to_merge_root.add_son(this_root)
            return heap_to_merge
