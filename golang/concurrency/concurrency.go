package main

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

func main() {
	// set the program to use only one processor
	// so there will be mutlithreading with concurrency
	runtime.GOMAXPROCS(1)

	var wg sync.WaitGroup
	wg.Add(3)

	fmt.Println("Starting Go Routines")
	go func() {
		defer wg.Done()

		time.Sleep(1 * time.Microsecond)
		for char := 'a'; char < 'a'+26; char++ {
			fmt.Printf("%c ", char)
		}
	}()

	go func() {
		defer wg.Done()

		for number := 1; number < 27; number++ {
			fmt.Printf("%d ", number)
		}
	}()

	go func() {
		defer wg.Done()

		for number := 1; number < 27; number++ {
			fmt.Printf("%d ", number)
		}
	}()

	fmt.Println("Waiting To Finish")

	// wait the program before exiting or proceeding further
	// until the goroutines in wait groups finish their executions
	wg.Wait()

	fmt.Println("\nTerminating Program")
}
