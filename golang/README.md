# Go Lang

## Go Routines

- goroutine is an independenty executing function, launched by a go statement.
- It has it's own call stack
    - It can grow and shrinks as required
    - Prior to version 1.2 the stack size started at 4K and now as of version 1.4 it starts at 8K.
- It's not an OS thread. It is much lighter than OS thread and can be called a green thread ( resembles the concept )
- goroutines are mutiplexed dynamically onto threads as needed to keep all the goroutines running.

## Channels

- A channel in Go provides a connection between two go routines, allowing the to communicate.

## GOMAXPROCS
- `runtime.GOMAXPROCS(0)` returns the max processes are used to run the program (argument has to be less than 1).
- `runtime.GOMAXPROCS(1)` sets the max processes to 1 process.
- By increasing the GOMAXPROCS value we can achieve parallel programming with goroutines
    - there has to more than 1 logical processor to achieve parallel programming
    - by default GOMAXPROCS values is set to max logical processor count in the system.

## Note

- When a go main function returns then all the go routines running if any will be killed and program will exit.

## References

- [Concurrency, Goroutines and GOMAXPROCS](https://www.ardanlabs.com/blog/2014/01/concurrency-goroutines-and-gomaxprocs.html)
- [Google I/O 2012 - Go Concurrency Patterns - YouTube](https://www.youtube.com/watch?v=f6kdp27TYZs)