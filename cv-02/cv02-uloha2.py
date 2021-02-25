# skelet programu prevzaty zo stranky cviceni
from time import sleep
from random import randint
from fei.ppds import Thread, Mutex, Semaphore
from fei.ppds import print


# ------- ULOHA 2: Znovupouzitelna bariera -------
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
            self.C = 0
            self.T.signal(self.N)
        self.M.unlock()
        self.T.wait()


def rendezvous(thread_name):
    sleep(randint(1, 10) / 10)
    print('rendezvous: %s' % thread_name)


def ko(thread_name):
    print('ko: %s' % thread_name)
    sleep(randint(1, 10) / 10)


def barrier_example(bariera1, bariera2, thread_id):
    """Kazde vlakno vykonava kod funkcie 'barrier_example'.
    Doplnte synchronizaciu tak, aby sa vsetky vlakna pockali
    nielen pred vykonanim funkcie 'ko', ale aj
    *vzdy* pred zacatim vykonavania funkcie 'rendezvous'.
    """

    while True:
        rendezvous(thread_id)
        bariera1.wait()
        ko(thread_id)
        bariera2.wait()


bariera1 = SimpleBarrier(5)
bariera2 = SimpleBarrier(5)

threads = list()
for i in range(5):
    t = Thread(barrier_example, bariera1, bariera2, f'Thread {i}')
    threads.append(t)
for t in threads:
    t.join()
