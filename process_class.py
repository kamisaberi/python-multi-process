import multiprocessing
import time


class MyProcess(multiprocessing.Process):
    id = 0

    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        print("process " + str(self.id))


if __name__ == "__main__":

    procs = []
    for i in range(100):
        pr = MyProcess(i)
        pr.start()
        procs.append(pr)
        time.sleep(3)
        i += 1

    for proc in procs:
        proc.join()
