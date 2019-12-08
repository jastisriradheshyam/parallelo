# Multithreading

- All threads in a process share access to the process resources.

# Multiprocessing

- Running mutiple processes on mutiple processors at same time by a program.

# Concurrency

- Concurrency in computer programming is to execute small processes or functions by interleaving the execution steps via time sharing slices. Only one small process or function can run at an instant.

# Parallel computing

- Run mutiple processes at an instance of time.
- Cannot be run on only one processer.
- To run a program parallelly
    - program should have small independent pieces of code
    - should be running on more than one physical processors

# Note

- Threads and processes can run in parallel.
- Multiprocessing is not equvalent to parallel processing
    - Multi processing program can run a program parallelly. But it is dependent on the OS how it schedules the processes.