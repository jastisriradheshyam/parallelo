# Multiprocessing

## GIL (Global Interpreter Lock)

- GIL is a mutex that protects access to python objects, preventing multiple threads from executing Python bytecode at once.

- This lock is necessary because CPython's memory management is not thread-safe.

- GIL must be held by the current thread before it can safely access Python objects. Without the lock, even the simplest operations could cause problems in a multi-threaded program.

## `multiprocessing` module

- `Process`
    - process object
    - creating a process: `process = Process(target=function_name, args=(first_arg,))`
    - starting the process: `process.start()`
    - block the calling thread until the process done executing or until the optional timeout occurs: `process.join([timeout])`
- `current_process()`
    - has attribute `name`, which is the name of the process.
- `Value`
    - create shared objects using shared memory which can be inherited by child processes.
    - Return a ctypes object allocated from shared memory.
- `Lock`
    - `lock.acquire()`
        - acquire the lock
    - `lock.release()`
        - release the lock
- `Pool`
    - A process pool object which controls a pool of worker processes to which jobs can be submitted.
        - `map`
            - A parallel equivalent of the map() built-in function (it supports only one iterable argument though). It blocks until the result is ready.
        - `close`
            - Prevents any more tasks from being submitted to the pool. Once all the tasks have been completed the worker processes will exit.
        - `join`
            - Wait for the worker processes to exit. One must call close() or terminate() before using join().
- `Queue`
    - The Queue class is a near clone of queue, for sharing the object accross the processes.

## `os` module

- `getpid()`
    - return the current pid of the function from which it was invoked.

## References:
[1] [GlobalInterpreterLock - Python Wiki](https://wiki.python.org/moin/GlobalInterpreterLock)  
[2]: [Thread safety - WikipediaThread safety - Wikipedia](https://en.wikipedia.org/wiki/Thread_safety)  
[3]: [17.2. multiprocessing — Process-based parallelism — Python 3.6.9 documentation](https://docs.python.org/3.6/library/multiprocessing.html)  
[4]: [Multiprocessing - YouTube](https://www.youtube.com/playlist?list=PL5tcWHG-UPH3SX16DI6EP1FlEibgxkg_6)