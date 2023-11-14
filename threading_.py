import threading
stop = False
def myfunc():
    global stop
    while stop == False:
        pass
thr1 = threading.Thread(target = myfunc)
thr1.start()
stop = True
while thr1.is_alive() == True:
    print('process')
print('поток завершился')