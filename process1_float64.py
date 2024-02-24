# Import libraries
from multiprocessing.shared_memory import SharedMemory
import struct

# Create a shared memory with a name
shared_mem = SharedMemory(name='MyMemory', size=1024, create=True)

while True:
    try:
        # Write data to shared memory
        shared_mem.buf[0:8] = struct.pack('d', 1.5) # Pack the float to bytes ('d' is for double-precision (64-bit) float)

        # Read data from shared memory
        data0 = shared_mem.buf[0:8]
        data1 = shared_mem.buf[9:17]
        data2 = shared_mem.buf[18:26]
        data3 = shared_mem.buf[27:35]

        # Print data from shared memory
        print(struct.unpack('d', data0)[0]) # Unpack the bytes to float
        print(struct.unpack('d', data1)[0]) # Unpack the bytes to float
        print(struct.unpack('d', data2)[0]) # Unpack the bytes to float
        print(struct.unpack('d', data3)[0]) # Unpack the bytes to float

    except KeyboardInterrupt:
        # Close the shared memory
        shared_mem.close()

        # Destroy the shared memory
        shared_mem.unlink()