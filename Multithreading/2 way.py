# import time
# start_time = time.time()
# for i in range(1000):
#     print(i**i)
#     for q in range(10):
#         print(q**2)
# print("--- %s seconds ---" % (time.time() - start_time))
import multithreading
import time
from Multithreading_test import Demo
demo = Demo(threads=3)

# Start threads
demo.start_threads()

# Adding task to queue
demo.add_task(1)
demo.add_task(2)
demo.add_task(3)

# Wait until queue is empty
demo.join()
