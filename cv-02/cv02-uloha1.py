# skelet programu prevzaty zo stranky cviceni
from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex
from fei.ppds import print


# ------- ULOHA 1: ADT SimpleBarrier -------
class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        self.C = 0
        self.M = Mutex()
        self.T = Semaphore(0)

    def wait(self):
        self.M.lock()
        self.C += 1
        if self.C == self.N:
            # self.C = 0 - pri znovupouziti
            self.T.signal(self.N)
        self.M.unlock()
        self.T.wait()


def barrier_example(barrier, thread_id):
    sleep(randint(1, 10) / 10)
    print("vlakno %d pred barierou" % thread_id)
    barrier.wait()
    print("vlakno %d po bariere" % thread_id)


sb = SimpleBarrier(10)

threads = list()
for i in range(10):
    t = Thread(barrier_example, sb, i)
    threads.append(t)
for t in threads:
    t.join()
