from fei.ppds import Thread, Semaphore, Mutex, print
from time import sleep

PRODUCE_TIME = 0.4
PROCESS_TIME = 0.2
NUMBER_OF_PRODUCENTS = 10
NUMBER_OF_CONSUMERS = 10
SIZE_OF_BUFFER = 5


class Item():
    def __init__(self, n):
        self.label = "Item " + str(n)
        self.id = n
        print("Vyprodukovany %d vyrobok" % self.id)


class Shared():
    def __init__(self):
        self.items = Semaphore(0)
        self.free = Semaphore(SIZE_OF_BUFFER)
        self.mutex = Mutex()
        self.item_id = 0
        self.queue = []


def fnc_produce(shared):
    sleep(PRODUCE_TIME)  # produce time
    shared.item_id += 1
    item = Item(shared.item_id)
    shared.free.wait()
    shared.mutex.lock()
    shared.queue.append(item)
    shared.mutex.unlock()
    shared.items.signal()


def fnc_process(shared):
    shared.items.wait()
    shared.mutex.lock()
    item = shared.queue.pop(0)
    print("Spracovany %d vyrobok" % item.id)
    shared.mutex.unlock()
    shared.free.signal()
    sleep(PROCESS_TIME)  # process time


sh = Shared()
threads = []

# najprv sa zamerne vytvaraju vlakna pre spracoovanie vyrobkov
for i in range(NUMBER_OF_CONSUMERS):
    threads.append(Thread(fnc_process, sh))
for i in range(NUMBER_OF_PRODUCENTS):
    threads.append(Thread(fnc_produce, sh))
for t in threads:
    t.join()
