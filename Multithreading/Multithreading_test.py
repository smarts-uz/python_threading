import multithreading
import time

class Demo(multithreading.MultiThread):
    def task(self, task):
        print(task)

task_list = range(1, 99 + 1)
demo = Demo(task_list, threads=3)

# Start
demo.start()


'''OR'''


