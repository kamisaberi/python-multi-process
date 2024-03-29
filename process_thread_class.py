import multiprocessing.process
from multiprocessing import Process
from threading import Thread
import time


class MyThread(Thread):
    id = 0

    def __init__(self, id, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.id = id

    def run(self):
        print(f"thread id : {self.id} , active process  : " + str(multiprocessing.current_process().name))


class MyProcess(Process):
    id = 0

    def __init__(self, id, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.id = id

    def run(self):
        print('process id :', self.id)
        threads = []
        for i in range(1, 11):
            thread = MyThread(i, name="thread " + str(i))
            thread.start()
            threads.append(thread)
            time.sleep(1)
        for thread in threads:
            thread.join()


if __name__ == "__main__":
    procs = []
    for i in range(1, 11):
        proc = MyProcess(i, name="process " + str(i))
        procs.append(proc)
        proc.start()
        time.sleep(3)
        # complete the processes
    for proc in procs:
        proc.join()
