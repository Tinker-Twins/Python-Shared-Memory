# Python Shared Memory

This project uses the `multiprocessing.shared_memory.SharedMemory` class, which allows a block of memory to be used by multiple Python processes. Since Python 2.6, `multiprocessing` is a built-in module. It ships with Python2 (>= Python 2.6) as well as Python3, no specific installation step is needed.

## What is SharedMemory?

- A `SharedMemory` object can be created and shared directly among multiple processes, or it can assigned a meaningful name attached to a process using that name.
- A `SharedMemory` has a fixed size (defined while creating it) and stores `byte` data.
- Python types can be converted to arrays of bytes and stored in a `SharedMemory` and read as arrays of bytes and converted back into Python types.
- A `SharedMemory` allows processes to read and write from the same memory, which is faster and more efficient than sharing data via message passing, such as via a `multiprocessing.Queue` or `multiprocessing.Pipe`.
