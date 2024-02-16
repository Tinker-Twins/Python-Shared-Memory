# Import library
from multiprocessing.shared_memory import SharedMemory

# Join an existing shared memory via its name
shared_mem = SharedMemory(name='MyMemory', create=False)

while True:
    try:
        # Write data to shared memory
        shared_mem.buf[1] = 2
        shared_mem.buf[2] = 3
        shared_mem.buf[3] = 4

        # Read data from shared memory
        data0 = shared_mem.buf[0]
        data1 = shared_mem.buf[1]
        data2 = shared_mem.buf[2]
        data3 = shared_mem.buf[3]

        # Print data from shared memory
        print(data0)
        print(data1)
        print(data2)
        print(data3)

    except KeyboardInterrupt:
        # Close the shared memory
        shared_mem.close()