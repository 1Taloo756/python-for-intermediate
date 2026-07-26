from multiprocessing import Process, Value, Array, Lock
import os
import time
from multiprocessing import Queue, Pool


def cube(number):
    return number * number * number


# def add_100(numbers, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         for i in range(len(numbers)):
#             with lock:
#                 numbers[i] += 1


# def square(numbers, q):
#     for i in numbers:
#         q.put(i * i)


# def make_negative(numbers, q):
#     for i in numbers:
#         q.put(-1 * i)


if __name__ == "__main__":
    # lock = Lock()
    # shared_array = Array("d", [0.0, 100.0, 200.0])
    # print("Array at beginning is ", shared_array[:])

    # p1 = Process(target=add_100, args=(shared_array, lock))
    # p2 = Process(target=add_100, args=(shared_array, lock))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()
    # print("Array at end is ", shared_array[:])
    # print("End main")

    # q = Queue()
    # numbers = range(1, 6)
    # p1 = Process(target=square, args=(numbers, q))
    # p2 = Process(target=make_negative, args=(numbers, q))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # while not q.empty():
    #     print(q.get())

    pool = Pool()
    numbers = range(10)

    # map, apply, join, close
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0]) give single argument

    pool.close()
    pool.join()

    print(result)
