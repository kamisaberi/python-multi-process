import threading
import  time

def thread_func(id):
    print("thread id = " + str(id))


for i in range(100):
    thread = threading.Thread(target=thread_func, args=(i,), name="th" + str(id))
    thread.start()
    time.sleep(1)

