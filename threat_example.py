import time
from threading import Thread, Lock, current_thread
from queue import Queue


# database_value = 0


# def increase(lock):
#     global database_value

# lock.acquire()
# local_copy = database_value
# local_copy += 1
# # database_value = local_copy
# time.sleep(0.1)
# database_value = local_copy
# lock.release()

# with lock:
#     local_copy = database_value
#     local_copy += 1
#     # database_value = local_copy
#     time.sleep(0.1)
#     database_value = local_copy


def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()


if __name__ == "__main__":
    # processes = []
    # num_processes = os.cpu_count()
    # lock = Lock()
    # print(f"start value {database_value}")
    # thread1 = Thread(target=increase, args=(lock,))
    # thread2 = Thread(target=increase, args=(lock,))
    # thread3 = Thread(target=increase)

    # thread1.start()
    # thread2.start()
    # thread3.start()

    # thread1.join()
    # thread2.join()
    # thread3.join()

    # print(f"end value {database_value}")
    lock = Lock()
    q = Queue()

    num_threads = 10

    for i in range(num_threads):
        threads = Thread(target=worker, args=(q, lock))
        threads.daemon = True
        threads.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print("End main")
