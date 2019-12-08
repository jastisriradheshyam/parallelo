import time
import logging
from multiprocessing import Process, Lock, Value
from multiprocessing import log_to_stderr, get_logger

# add 500 to the total


def add_500_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value += 5
        lock.release()

# sub 500 to the total


def sub_500_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value -= 5
        lock.release()


if __name__ == '__main__':

    # create shared object
    total = Value('i', 500)

    # lock object
    lock = Lock()

    log_to_stderr()
    logger = get_logger()
    logger.setLevel(logging.INFO)

    add_process = Process(target=add_500_lock, args=(total, lock))
    sub_process = Process(target=sub_500_lock, args=(total, lock))

    # start the process
    add_process.start()
    sub_process.start()

    # block the current thread untill both processes
    # complete their processing
    add_process.join()
    sub_process.join()

    print(total.value)
