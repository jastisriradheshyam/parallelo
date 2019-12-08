from multiprocessing import Process, Queue

def square(numbers,queue):
    """Square the numbers"""
    for i in numbers:
        queue.put(i*i)

def cube(numbers, queue):
    """Cube the numbers"""
    for i in numbers:
        queue.put(i*i*i)

if __name__ == '__main__':
    numbers = range(5)
    # shared queue
    queue = Queue()

    # create the process
    square_process = Process(target=square, args=(numbers, queue))
    cube_process = Process(target=cube, args=(numbers, queue))

    # start the process
    square_process.start()
    cube_process.start()

    # block the current thread untill both processes
    # complete their processing
    square_process.join()
    cube_process.join()

    # printing the queue
    while not queue.empty():
        print(queue.get())
