from multiprocessing import Process
import time


def process_func(id):
    print('process id :', id)


if __name__ == "__main__" :
    procs = []
    for i in range(1000):
        proc = Process(target=process_func, args=(i,))
        procs.append(proc)
        proc.start()
        time.sleep(3)

        # complete the processes
    for proc in procs:
        proc.join()
