import os
import time
from multiprocessing import Process, current_process


def square(numbers):
    """Square and print the numbers"""
    for number in numbers:
        time.sleep(0.5)
        result = number * number
        print(f"The number {number} squares to {result}.")

    process_id = os.getpid()
    print(f"Process ID: {process_id}")

    process_name = current_process().name
    print(f"Process Name:{process_name}")


if __name__ == '__main__':
    processes = []

    numbers = range(100)

    # spawn the processes
    for i in range(50):
        process = Process(target=square, args=(numbers,))
        processes.append(process)

        # spawning of process
        process.start()

    # hold the flow untill all the processes complete the execution
    for process in processes:
        process.join()

    print("done multiprocessing")
