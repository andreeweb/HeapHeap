import random
import time
from Heap.BinaryHeapQueue import BinaryHeapQueue
from Heap.BinomialHeapQueue import BinomialHeapQueue
from Heap.DHeapNode import DHeapNode
from Utils.Generator import Generator
from Heap.DHeapQueue import DHeapQueue
from Heap.HeapSort import HeapSort


# global log time
global log_time


def log(value):
    """
    Used to write on log file.
    :return:
    """

    global log_time

    if log_time is not None:
        f = open("./log_" + str(int(log_time)) + ".txt", "a")
    else:
        f = open("./log_" + str(time.time()) + ".txt", "a")

    f.write(value)

    if True:
        print(value)


def option_insert_delete(rnd_numb):

    p = 0
    while True:
        p = input("\n Please insert the probability\n")
        try:
            if 0 <= float(p) <= 1:
                break
            else:
                print("Please insert a valid probability! (Probability must be between 0 and 1)")
        except ValueError:
            print("Please insert a valid probability!")
            continue

    while True:

        select_queue = input(
            "\n Please select the data structure with which you want to perform test.\n "
            "1 - 2Heap \n"
            " 2 - 3Heap \n"
            " 3 - 4Heap \n"
            " 4 - 6Heap \n"
            " 5 - 8Heap \n"
            " 6 - 10Heap \n"
            " 7 - 16Heap \n"
            " 8 - BinaryHeap \n"
            " 9 - BinomialHeap \n"
            " q - Quit \n")
        try:
            if str(select_queue) == 'q':
                break
            elif int(select_queue) == 1:
                option_insert_delete_heap(rnd_numb, p, 2)
            elif int(select_queue) == 2:
                option_insert_delete_heap(rnd_numb, p, 3)
            elif int(select_queue) == 3:
                option_insert_delete_heap(rnd_numb, p, 4)
            elif int(select_queue) == 4:
                option_insert_delete_heap(rnd_numb, p, 6)
            elif int(select_queue) == 5:
                option_insert_delete_heap(rnd_numb, p, 8)
            elif int(select_queue) == 6:
                option_insert_delete_heap(rnd_numb, p, 10)
            elif int(select_queue) == 7:
                option_insert_delete_heap(rnd_numb, p, 16)
            elif int(select_queue) == 8:
                option_insert_delete_binary_heap(rnd_numb, p)
            elif int(select_queue) == 9:
                option_insert_delete_binomial_heap(rnd_numb, p)
            else:
                print("Please select a valid option!")
        except ValueError:
            print("Please select a valid option!")
            continue


def option_insert_delete_heap(rnd_numb, p, d):

    log("**************************\n\n")

    log("Start insert half input in " + str(d) + "Heap data structure" + "\n")
    start_ordering_time = time.time()

    count = int(len(rnd_numb)/2)

    pq = DHeapQueue(d)
    for i in range(count):
        pq.insert(rnd_numb[i][0], rnd_numb[i][0])

    for count in range(len(rnd_numb)):

        k = random.uniform(0.0, 1.0)

        if float(k) < float(p):
            pq.insert(rnd_numb[count][0], rnd_numb[count][0])
        else:
            pq.delete_min()

    log("End insert/delete in: " + str(time.time() - start_ordering_time) + "\n\n")


def option_insert_delete_binary_heap(rnd_numb, p):
    print(rnd_numb)


def option_insert_delete_binomial_heap(rnd_numb, p):
    print(rnd_numb)


def option_order(rnd_numb):

    while True:

        select_queue = input(
            "\n Please select the data structure with which you want to perform test.\n "
            "1 - 2Heap \n"
            " 2 - 3Heap \n"
            " 3 - 4Heap \n"
            " 4 - 6Heap \n"
            " 5 - 8Heap \n"
            " 6 - 10Heap \n"
            " 7 - 16Heap \n"
            " 8 - BinaryHeap \n"
            " 9 - BinomialHeap \n"
            " q - Quit \n")
        try:
            if str(select_queue) == 'q':
                break
            elif int(select_queue) == 1:
                heapsort_heap(rnd_numb, 2)
            elif int(select_queue) == 2:
                heapsort_heap(rnd_numb, 3)
            elif int(select_queue) == 3:
                heapsort_heap(rnd_numb, 4)
            elif int(select_queue) == 4:
                heapsort_heap(rnd_numb, 6)
            elif int(select_queue) == 5:
                heapsort_heap(rnd_numb, 8)
            elif int(select_queue) == 6:
                heapsort_heap(rnd_numb, 10)
            elif int(select_queue) == 7:
                heapsort_heap(rnd_numb, 16)
            elif int(select_queue) == 8:
                heapsort_binary_heap(rnd_numb)
            elif int(select_queue) == 9:
                heapsort_binomial_heap(rnd_numb)
            else:
                print("Please select a valid option!")
        except ValueError:
            print("Please select a valid option!")
            continue


def heapsort_heap(rnd_numb, d):

    log("**************************\n\n")

    log("Start ordering input with " + str(d) + "Heap data structure" + "\n")
    start_ordering_time = time.time()

    pq = DHeapQueue(d)
    for i in range(len(rnd_numb)):
        pq.insert(rnd_numb[i][0], rnd_numb[i][0])

    log("End ordering in: " + str(time.time() - start_ordering_time) + "\n\n")
    log("Input ordered \n" + str(HeapSort.heapsort_support(pq)) + "\n\n")


def heapsort_binary_heap(rnd_numb):

    log("**************************\n")

    log("Start ordering input with BinaryHeapQueue data structure" + "\n")
    start_ordering_time = time.time()

    pq = BinaryHeapQueue()
    for i in range(len(rnd_numb)):
        pq.insert(rnd_numb[i][0], rnd_numb[i][0])

    log("End ordering in: " + str(time.time() - start_ordering_time) + "\n\n")
    log("Input ordered \n" + str(HeapSort.heapsort_support(pq)) + "\n\n")


def heapsort_binomial_heap(rnd_numb):

    log("**************************\n")

    log("Start ordering input with BinomialHeapQueue data structure" + "\n")
    start_ordering_time = time.time()

    pq = BinomialHeapQueue(32)
    for i in range(len(rnd_numb)):
        pq.insert(rnd_numb[i][0], rnd_numb[i][0])

    log("End ordering in: " + str(time.time() - start_ordering_time) + "\n\n")
    log("Input ordered \n" + str(HeapSort.heapsort_support(pq)) + "\n\n")


def divider():
    return "---------------------------------------- \n"

if __name__ == "__main__":

    log_time = time.time()

    log(divider())
    log("Start execution:" + str(int(log_time)) + "\n\n")

    input_size = 0
    seed = 0

    while True:
        input_size = input("Please insert the size of input (Size must be between 5000 and 50000)\n")
        try:
            if 0 < int(input_size) <= 50000:
                break
            else:
                print("Please insert a valid number!")
        except ValueError:
            print("Please insert a valid number!")

    while True:
        seed = input("Please insert the seed of input\n")
        try:
            if int(seed) > 0:
                break
            else:
                print("Please insert a valid seed! (Seed must be > 0)")
        except ValueError:
            print("Please insert a valid seed!")
            continue

    random_numbers = Generator.generate(int(seed), int(input_size))

    log("Input size: \n" + input_size + "\n\n")
    log("Seed:\n" + seed + "\n\n")
    log("Input:\n" + str(random_numbers) + "\n\n")

    while True:
        option_selected = input(
            '\n Please select one option:\n 1 - Test insert/delete \n 2 - Test Heapsort \n q - Quit \n\n')
        try:
            if str(option_selected) == 'q':
                break
            elif int(option_selected) == 1:
                option_insert_delete(random_numbers)
            elif int(option_selected) == 2:
                option_order(random_numbers)
            else:
                print("Please insert a valid option!")
        except ValueError:
            print("Please insert a valid option!")
            continue

    end = time.time()

    log("End execution: " + str(end - log_time) + "\n\n")
    log(divider())
