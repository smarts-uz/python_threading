# # importing the multiprocessing module
# import multiprocessing
#
# def print_cube(num):
# 	"""
# 	function to print cube of given num
# 	"""
# 	print("Cube: {}".format(num * num * num))
#
# def print_square(num):
# 	"""
# 	function to print square of given num
# 	"""
# 	print("Square: {}".format(num * num))
#
# if __name__ == "__main__":
# 	# creating processes
# 	p1 = multiprocessing.Process(target=print_square, args=(20, ))
# 	p2 = multiprocessing.Process(target=print_cube, args=(20, ))
#
# 	# starting process 1
# 	p1.start()
# 	# starting process 2
# 	p2.start()
#
# 	# wait until process 1 is finished
# 	p1.join()
# 	# wait until process 2 is finished
# 	p2.join()
#
# 	# both processes finished
# 	print("Done!")

# importing the multiprocessing module
import multiprocessing
import os

def worker1():
	# printing process id
	print("ID of process running worker1: {}".format(os.getpid()))

def worker2():
	# printing process id
	print("ID of process running worker2: {}".format(os.getpid()))

if __name__ == "__main__":
	# printing main program process id
	print("ID of main process: {}".format(os.getpid()))

	# creating processes
	p1 = multiprocessing.Process(target=worker1)
	p2 = multiprocessing.Process(target=worker2)

	# starting processes
	p1.start()
	p2.start()

	# process IDs
	print("ID of process p1: {}".format(p1.pid))
	print("ID of process p2: {}".format(p2.pid))

	# wait until processes are finished
	p1.join()
	p2.join()

	# both processes finished
	print("Both processes finished execution!")

	# check if processes are alive
	print("Process p1 is alive: {}".format(p1.is_alive()))
	print("Process p2 is alive: {}".format(p2.is_alive()))
