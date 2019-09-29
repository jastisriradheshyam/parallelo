import os

from multiprocessing import Process, current_process


def square(number):
    """Square the number"""
    result = number * number
    print(f"The number {number} squares to {result}.")

    process_id = os.getpid()
    print(f"Process ID: {process_id}")

    process_name = current_process().name
    print(f"Process Name:{process_name}")


if __name__ == '__main__':
    processes = []

    numbers = range(5)
    for number in numbers:
        process = Process(target=square, args=(number,))
        processes.append(process)

        # spawning of process
        process.start()
