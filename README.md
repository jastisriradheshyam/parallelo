# Process
- A process is a program in execution.
- Every process has their own address space.
- A process comprises of one or more threads of execution.

# Thread
- Threads are part of a process that share various resources, like address space.
- Threads can communicate directly through shared memory.

# Multi-threading

- All threads in a process share access to the process resources.

# Multiprocessing

- Running multiple processes on multiple processors at same time by a program.

# Concurrency

- Concurrency in computer programming is to execute small processes or functions by interleaving the execution steps via time sharing slices. Only one small process or function can run at an instant.

# Parallel computing

- Run multiple processes at an instance of time.
- Cannot be run on only one processor.
- To run a program parallel
    - program should have small independent pieces of code
    - should be running on more than one physical processors

# Note

- Threads and processes can run in parallel.
- Multiprocessing is not equivalent to parallel processing
    - Multi processing program can run a program parallel. But it is dependent on the OS how it schedules the processes.