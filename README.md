# multithreading_in_python

Python Session No. 20 
Summary 03-01-2024

Thread
In Python, a thread is like a separate to-do list that can work on tasks at the same time as other threads. They're useful for doing things simultaneously, but keep in mind that due to a limitation called the Global Interpreter Lock (GIL), they might not be great for certain types of tasks that need a lot of computing power.
Single-threaded
Single-threaded in Python means that the program executes one instruction at a time within a single sequence. It processes tasks sequentially, which can be straightforward but may lead to slower performance, especially for concurrent or parallelizable operations. It executes commands sequentially, potentially causing delays when dealing with multiple tasks concurrently.



Multithreading in Python
Multithreading in Python allows a program to perform multiple tasks concurrently, enhancing efficiency. It's useful for tasks involving waiting, like I/O operations, as threads can continue other work while waiting. However, for CPU-intensive tasks, multiprocessing may be more effective due to Python's Global Interpreter Lock (GIL).


Synchronous programming in Python
Synchronous programming in Python means executing tasks one after the other, where each task must complete before the next one starts. It follows a sequential flow, waiting for each operation to finish before moving on to the next, which can lead to potential inefficiencies in handling tasks.

I/O-bound operation
In Python, an I/O-bound operation refers to a task that spends a significant amount of time waiting for input/output operations to complete, such as reading or writing to files or making network requests. Multithreading is often beneficial for handling I/O-bound tasks as it allows the program to continue with other activities while waiting for these operations to finish.


Use multithreading for I/O-bound operations in Python when tasks involve waiting for input/output, like reading files or making network requests. It's helpful to keep the program responsive during waiting periods. However, for CPU-bound tasks that require intense computation, consider alternatives like multiprocessing due to Python's Global Interpreter Lock (GIL), which can limit the effectiveness of multithreading for CPU-bound operations.

Global Interpreter Lock.
In Python, GIL stands for Global Interpreter Lock. It is a mechanism that allows only one thread to execute Python bytecode at a time in a single process. This means that even on multi-core systems, only one thread can execute Python code at any given moment.
The GIL can impact the performance of multi-threaded Python programs because it limits the parallel execution of threads. However, it primarily affects CPU-bound tasks rather than I/O-bound tasks.

➡  This Python code defines two functions, `coffee` and `tea`, simulating the preparation of coffee and tea, each with a delay using `time.sleep`. The main function then calls these two functions sequentially, measures the total time consumed for both tasks, and prints the result.


The code simulates making coffee and tea, measures the time it takes for both tasks, and prints the total time consumed by the CPU. The output will look like:


➡ Now, this Python code defines two functions, `coffee` and `tea`, simulating the preparation of coffee and tea, respectively. Threading is used to run these functions concurrently. The main function starts the threads, prints a message, and then waits for both threads to finish before printing another message. The code also measures the total time consumed by the CPU.


The program starts preparing coffee and tea concurrently using threads. It then prints "hi i m in main function" and waits for both threads to finish. After completion, it prints messages indicating the finish of coffee and tea, followed by the total time consumed by the CPU (in this example, 3.00234 seconds).



➡ The code uses threading to perform a CPU-bound operation of incrementing a variable up to 100 million. However, threading doesn't provide true parallelism in Python due to the Global Interpreter Lock (GIL), and the code measures the total time consumed by the CPU for this task.


The code prints the value of the variable 'i' (which is 100000001) and the total time consumed by the CPU for the entire operation. The output does not involve threading, as the function is executed in a single thread.


➡ The code uses threading to perform a CPU-bound operation of incrementing a variable up to 100 million in three separate threads. However, due to the Global Interpreter Lock (GIL) in Python, true parallelism is limited. The code measures the total time consumed by the CPU for this task and prints the result.


The code launches three threads to separately increment a variable up to 100 million. However, due to the Global Interpreter Lock (GIL) in Python, true parallelism is limited, and the threads effectively run sequentially. The output includes the final value of the variable from each thread and the total time consumed by the CPU for the entire operation. The actual output may vary, but it will reflect the limitations of threading in Python due to the GIL.





In Python, multithreading does not provide true parallelism due to the Global Interpreter Lock (GIL). The GIL allows only one thread to execute Python bytecode at a time, limiting simultaneous execution. Multithreading is more effective for I/O-bound tasks than CPU-bound tasks. For genuine parallelism, consider using multiprocessing.
