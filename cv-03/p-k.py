from fei.ppds import Thread, Semaphore, Mutex


class Shared():
    def __init__(self):
        self.items = Semaphore(0)
        self.free = Semaphore(10)
        self.mutex = Mutex()


def fnc_produce(shared):
    pass


def fnc_process(shared):
    pass


def fnc_p_k(shared):
    pass


sh = Shared()
threads = []

for i in range(10):
    threads.append(Thread(fnc_p_k, sh))
for t in threads:
    t.join()
