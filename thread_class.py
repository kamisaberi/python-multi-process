import threading
import time


class MyThread(threading.Thread):
    id = 0

    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        print("thread " + str(self.id))


if __name__ == "__main__":

    thrds = []
    for i in range(100):
        th = MyThread(i)
        th.start()
        thrds.append(th)
        time.sleep(3)
        i += 1

    for thrd in thrds:
        thrd.join()
