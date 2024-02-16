# Import library
from multiprocessing.shared_memory import SharedMemory

# Create a shared memory with a name
shared_mem = SharedMemory(name='MyMemory', size=1024, create=True)

while True:
    try:
        # Write data to shared memory
        shared_mem.buf[0] = 1

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

        # Destroy the shared memory
        shared_mem.unlink()