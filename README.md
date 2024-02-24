# Python Shared Memory

This project uses the `multiprocessing.shared_memory.SharedMemory` class, which allows a block of memory to be used by multiple Python processes. Since Python 2.6, `multiprocessing` is a built-in module. It ships with Python2 (>= Python 2.6) as well as Python3, no specific installation step is needed.

## What is SharedMemory?

- A `SharedMemory` object can be created and shared directly among multiple processes, or it can assigned a meaningful name attached to a process using that name.
- A `SharedMemory` has a fixed size (defined while creating it) and stores `byte` data.
- Python types can be converted to arrays of bytes and stored in a `SharedMemory` and read as arrays of bytes and converted back into Python types.
- A `SharedMemory` allows processes to read and write from the same memory, which is faster and more efficient than sharing data via message passing, such as via a `multiprocessing.Queue` or `multiprocessing.Pipe`.

## How to Use SharedMemory?

A `SharedMemory` can be created in a process by calling the constructor and specifying a `size` in bytes and the `create` argument to `True`. A shared memory object can be assigned a meaningful name via the `name` attribute to the constructor.
```python
# Create a shared memory with a name
shared_mem = SharedMemory(name='MyMemory', size=1024, create=True)
```

Another process can access a shared memory via its `name`. This is called attaching to a shared memory. This can be achieved by specifying the `name` of the shared memory that has already been created and setting the `create` argument to `False` (the default).
```python
# Attach to a shared memory
shared_mem = SharedMemory(name='MyMemory', create=False)
```

Once created, data can be stored in the shared memory via the `buf` attribute that acts like an array of bytes.
```python
# Write data to shared memory
shared_mem.buf[0] = 1
```

Data can be read from the `buf` attribute in the same manner.
```python
# Read data from shared memory
data = shared_mem[0]
```

Once a process is finished using the shared memory, it can be closed to signal that access is no longer required. All processes should close the shared memory once they are finished with it.
```python
# Close access to the shared memory
shared_mem.close()
```

Once all processes are finished with the shared memory, it must be explicitly released. This can be achieved by calling the `unklink()` method. Ideally, the process that created the shared memory would also release it.
```python
# Destroy the shared memory
shared_mem.unlink()
```

## Examples of Using SharedMemory

This project implements two simple and intuitive examples of `SharedMemory` with two Python processes:
- **`uint8` Example:**
  - [`process1_uint8.py`](process1_uint8.py) creates the shared memory and writes the first byte.
  - [`process2_uint8.py`](process2_uint8.py) joins the shared memory and writes the second, third and fourth bytes.
  - [`process1_uint8.py`](process1_uint8.py) and [`process2_uint8.py`](process2_uint8.py) both read and print the first, second, third and fourth bytes.
  - [`process1_uint8.py`](process1_uint8.py) and [`process2_uint8.py`](process2_uint8.py) both close the shared memory before terminating.
  - [`process1_uint8.py`](process1_uint8.py) releases the shared memory before terminating.
    
    Terminal 1:
    ```bash
    python3 process1_uint8.py
    ```
    Terminal 2:
    ```bash
    python3 process2_uint8.py
    ```
- **`float64` Example:**
  - [`process1_float64.py`](process1_float64.py) creates the shared memory and writes the first byte array.
  - [`process2_float64.py`](process2_float64.py) joins the shared memory and writes the second, third and fourth byte  arrays.
  - [`process1_float64.py`](process1_float64.py) and [`process2_float64.py`](process2_float64.py) both read and print the first, second, third and fourth byte arrays.
  - [`process1_float64.py`](process1_float64.py) and [`process2_float64.py`](process2_float64.py) both close the shared memory before terminating.
  - [`process1_float64.py`](process1_float64.py) releases the shared memory before terminating.
    
    Terminal 1:
    ```bash
    python3 process1_float64.py
    ```
    Terminal 2:
    ```bash
    python3 process2_float64.py
    ```

**Notes:**
- Launching `process1` alone will print the default value for all the bytes that haven't yet been written to (since they are written by `process2`). The bytes written by `process1` itself will be updated and printed accordingly.
- Launching `process2` before `process1` will throw an error since the shared memory has not yet been created.

## Reference
[Jason Brownlee](https://superfastpython.com/about), "How to Use SharedMemory in Python", in [_PYTHON MULTIPROCESSING_](https://superfastpython.com/category/multiprocessing), March 24, 2023. [Online]. Available: https://superfastpython.com/multiprocessing-sharedmemory
