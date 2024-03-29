import multiprocessing.process
from multiprocessing import Process
from threading import Thread
import time


def thread_func(process_id, thread_id):
    print(
        f"process id : {process_id} , thread id : {thread_id} , active process  : " + str(multiprocessing.current_process().name))


def process_func(process_id):
    print('process id :', process_id)
    threads = []
    for i in range(1, 11):
        thread = Thread(target=thread_func, args=(process_id, i), name="thread " + str(i))
        thread.start()
        threads.append(thread)
        time.sleep(1)
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    procs = []
    for i in range(1, 11):
        proc = Process(target=process_func, args=(i,), name="process " + str(i))
        procs.append(proc)
        proc.start()
        time.sleep(3)

        # complete the processes
    for proc in procs:
        proc.join()
