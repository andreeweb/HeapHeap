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

    def get_heap_sons(self):
        res = []
        count = 0
        length = len(self.root.sons)
        while length > 0:
            current = self.root.sons[count]
            new_heap = BinomialHeap(None, None)
            new_heap.root = current
            res.append(new_heap)
            count += 1
            length -= 1
        return res

    def print_heap(self):
        queue = [self.root, None]
        s = ""
        while not len(queue) == 0:
            current = queue.pop(0)
            count = 0
            if current is None:
                s += "\n"
            else:
                s += "[" + str(current.elem) + ", " + str(current.key) + "] "
                length = len(current.sons)
                while length > 0:
                    f = current.sons[count]
                    queue.append(f)
                    count += 1
                    length -= 1
                queue.append(None)
        print(s)


