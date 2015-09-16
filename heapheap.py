import random
import time
from Heap.BinaryHeapQueue import BinaryHeapQueue
from Heap.BinomialHeapQueue import BinomialHeapQueue
from Utils.Generator import Generator
from Heap.DHeapQueue import DHeapQueue
from Heap.HeapSort import HeapSort
import matplotlib.pyplot as plot

# global log time
log_time = 0


def log(value):
    """
    Used to write on log file.
    :return:
    """

    global log_time

    if log_time is not None:
        f = open("./logs/log_" + str(int(log_time)) + ".txt", "a")
    else:
        f = open("./logs/log_" + str(time.time()) + ".txt", "a")

    f.write(value)

    if True:
        print(value)


def option_insert_delete(rnd_numb):

    axis_y = []
    axis_x = []
    name = []

    p = 0
    while True:
        p = input("\n Please insert the probability\n")
        try:
            if 0 <= float(p) <= 1:
                log("P:" + p + "\n\n")
                break
            else:
                print("Please insert a valid probability! (Probability must be between 0 and 1)")
        except ValueError:
            print("Please insert a valid probability!")
            continue

    while True:

        select_queue = input(
            "\n Please select the data structure with which you want to perform test.\n "
            "1  - 2Heap \n"
            " 2  - 3Heap \n"
            " 3  - 4Heap \n"
            " 4  - 6Heap \n"
            " 5  - 8Heap \n"
            " 6  - 10Heap \n"
            " 7  - 16Heap \n"
            " 8  - BinaryHeap \n"
            " 9  - BinomialHeap \n"
            " 10 - Perform test on all queue\n"
            " b  - Back \n")
        try:
            if str(select_queue) == 'b':
                break
            elif int(select_queue) == 1:
                insert_delete_heap(rnd_numb, p, 2, DHeapQueue, axis_x, axis_y, name)
                plot_insert_delete_option(axis_x, axis_y, name)
            elif int(select_queue) == 2:
                insert_delete_heap(rnd_numb, p, 3, DHeapQueue, axis_x, axis_y, name)
                plot_insert_delete_option(axis_x, axis_y, name)
            elif int(select_queue) == 3:
                insert_delete_heap(rnd_numb, p, 4, DHeapQueue, axis_x, axis_y, name)
                plot_insert_delete_option(axis_x, axis_y, name)
            elif int(select_queue) == 4:
                insert_delete_heap(rnd_numb, p, 6, DHeapQueue, axis_x, axis_y, name)
                plot_insert_delete_option(axis_x, axis_y, name)
            elif int(select_queue) == 5:
                insert_delete_heap(rnd_numb, p, 8, DHeapQueue, axis_x, axis_y, name)
                plot_insert_delete_option(axis_x, axis_y, name)
            elif int(select_queue) == 6:
                insert_delete_heap(rnd_numb, p, 10, DHeapQueue, axis_x, axis_y, name)
                plot_insert_delete_option(axis_x, axis_y, name)
            elif int(select_queue) == 7:
                insert_delete_heap(rnd_numb, p, 16, DHeapQueue, axis_x, axis_y, name)
                plot_insert_delete_option(axis_x, axis_y, name)
            elif int(select_queue) == 8:
                insert_delete_heap(rnd_numb, p, None, BinaryHeapQueue, axis_x, axis_y, name)
                plot_insert_delete_option(axis_x, axis_y, name)
            elif int(select_queue) == 9:
                insert_delete_heap(rnd_numb, p, 32, BinomialHeapQueue, axis_x, axis_y, name)
                plot_insert_delete_option(axis_x, axis_y, name)
            elif int(select_queue) == 10:
                insert_delete_heap(rnd_numb, p, 2, DHeapQueue, axis_x, axis_y, name)
                insert_delete_heap(rnd_numb, p, 3, DHeapQueue, axis_x, axis_y, name)
                insert_delete_heap(rnd_numb, p, 4, DHeapQueue, axis_x, axis_y, name)
                insert_delete_heap(rnd_numb, p, 6, DHeapQueue, axis_x, axis_y, name)
                insert_delete_heap(rnd_numb, p, 8, DHeapQueue, axis_x, axis_y, name)
                insert_delete_heap(rnd_numb, p, 10, DHeapQueue, axis_x, axis_y, name)
                insert_delete_heap(rnd_numb, p, 16, DHeapQueue, axis_x, axis_y, name)
                insert_delete_heap(rnd_numb, p, None, BinaryHeapQueue, axis_x, axis_y, name)
                # insert_delete_heap(rnd_numb, p, 32,  BinomialHeapQueue, axis_x, axis_y)
                plot_insert_delete_option(axis_x, axis_y, name)
            else:
                print("Please select a valid option!")
        except Exception as e:
            print("Please select a valid option!" + str(e))
            continue


def insert_delete_heap(rnd_numb, p, d, cls, axis_x, axis_y, name):

    plot_value_x = []
    plot_value_y = []

    start_ordering_time = time.time()

    # identify the queue
    if cls == DHeapQueue:
        pq = DHeapQueue(d)
        log("\nStart execution on " + str(d) + "Heap data structure" + "\n")
        name.append(str(d) + "Heap")

    elif cls == BinaryHeapQueue:
        pq = BinaryHeapQueue()
        log("\nStart execution on BinaryHeap data structure" + "\n")
        name.append("BinaryHeap")

    else:
        pq = BinomialHeapQueue(d)
        log("\nStart execution on BinomialHeap data structure" + "\n")
        name.append("BinomialHeap")

    # how many insert before start with the insert/delete algorithm
    count = int(len(rnd_numb)/2)

    # perform some insert
    for i in range(count):
        pq.insert(rnd_numb[i][0], rnd_numb[i][0])

    # start to insert with probability of 0 < p < 1, delete with probability of 1-p
    action_time = time.time()
    for i in range(count, len(rnd_numb)):
        k = random.uniform(0.0, 1.0)
        if float(k) < float(p):
            pq.insert(rnd_numb[count][0], rnd_numb[count][0])
        else:
            pq.delete_min()
        if i % 1500 == 0:
            plot_value_y.append(float((time.time() - action_time)) * 1000)
            plot_value_x.append(i)
            action_time = time.time()

    axis_x.append(plot_value_x)
    axis_y.append(plot_value_y)

    log("\nX values: " + str(plot_value_x) + "\n")
    log("Y values: " + str(plot_value_y) + "\n\n")

    log("\nEnd execution in: " + str(time.time() - start_ordering_time) + "\n\n")


def option_order(rnd_numb):

    while True:

        select_queue = input(
            "\n Please select the data structure with which you want to perform test.\n "
            "1  - 2Heap \n"
            " 2  - 3Heap \n"
            " 3  - 4Heap \n"
            " 4  - 6Heap \n"
            " 5  - 8Heap \n"
            " 6  - 10Heap \n"
            " 7  - 16Heap \n"
            " 8  - BinaryHeap \n"
            " 9  - BinomialHeap \n"
            " 10 - Perform test on all queue\n"
            " b  - Back \n")
        try:
            if str(select_queue) == 'b':
                break
            elif int(select_queue) == 1:
                heapsort(rnd_numb, 2, DHeapQueue)
            elif int(select_queue) == 2:
                heapsort(rnd_numb, 3, DHeapQueue)
            elif int(select_queue) == 3:
                heapsort(rnd_numb, 4, DHeapQueue)
            elif int(select_queue) == 4:
                heapsort(rnd_numb, 6, DHeapQueue)
            elif int(select_queue) == 5:
                heapsort(rnd_numb, 8, DHeapQueue)
            elif int(select_queue) == 6:
                heapsort(rnd_numb, 10, DHeapQueue)
            elif int(select_queue) == 7:
                heapsort(rnd_numb, 16, DHeapQueue)
            elif int(select_queue) == 8:
                heapsort(rnd_numb, None, BinaryHeapQueue)
            elif int(select_queue) == 9:
                heapsort(rnd_numb, 32, BinomialHeapQueue)
            elif int(select_queue) == 10:
                heapsort(rnd_numb, 2, DHeapQueue)
                heapsort(rnd_numb, 3, DHeapQueue)
                heapsort(rnd_numb, 4, DHeapQueue)
                heapsort(rnd_numb, 6, DHeapQueue)
                heapsort(rnd_numb, 8, DHeapQueue)
                heapsort(rnd_numb, 10, DHeapQueue)
                heapsort(rnd_numb, 16, DHeapQueue)
                heapsort(rnd_numb, None, BinaryHeapQueue)
                # heapsort(rnd_numb, 32, BinomialHeapQueue, axis_x, axis_y)
            else:
                print("Please select a valid option!")
        except ValueError:
            print("Please select a valid option!")
            continue


def heapsort(rnd_numb, d, cls):

    log("\n\n **************************\n")

    start_ordering_time = time.time()

    # identify the queue
    if cls == DHeapQueue:
        pq = DHeapQueue(d)
        log("Start heapsort with " + str(d) + "Heap data structure" + "\n")
    elif cls == BinaryHeapQueue:
        pq = BinaryHeapQueue()
        log("Start heapsort with BinaryHeap data structure" + "\n")
    else:
        pq = BinomialHeapQueue(d)
        log("Start heapsort with BinomialHeap data structure" + "\n")

    # insert input on heap structure
    for i in range(len(rnd_numb)):
        pq.insert(rnd_numb[i][0], rnd_numb[i][0])

    # do heapsort!
    result = HeapSort.heapsort_support(pq)

    timestamp = str(time.time() - start_ordering_time)

    log("End ordering in: " + timestamp + "\n\n")
    log("Input ordered \n" + str(result[:35]) + "...\n\n")


def divider():
    return "\n ---------------------------------------- \n"


def plot_insert_delete_option(x_values, y_values, name):

    # print(x_values)
    # print(y_values)
    # print(name)

    plot.title("Priority Queue")
    plot.xlabel("Length of list (number)")
    plot.ylabel("Time taken (milliseconds)")

    y_min = 0
    y_max = 0

    for i in range(len(x_values)):
        plot.plot(x_values[i], y_values[i], label=str(name[i]))
        if max(y_values[i]) > y_max:
            y_max = max(y_values[i])
        if min(y_values[i]) < y_min:
            y_min = min(y_values[i])

    plot.axis([x_values[0][0], x_values[0][-1], y_min, y_max + 10])
    plot.legend(loc='upper left')
    plot.show()


if __name__ == "__main__":

    log_time = time.time()

    log(divider())

    input_size = 0
    seed = 0

    while True:
        input_size = input("Please insert the size of input (Size must be between 5000 and 50000)\n")
        try:
            if 5000 <= int(input_size) <= 50000:
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
    log("Input:\n" + str(random_numbers[:35]) + "...\n\n")

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

    log(divider())
