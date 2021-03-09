from fei.ppds import Thread, Semaphore, Mutex, print


class Item():
    def __init__(self, n):
        self.label = "Item " + str(n)
        self.id = n
        print("Vyprodukovany %d vyrobok" % self.id)


class Shared():
    def __init__(self):
        self.items = Semaphore(0)
        self.free = Semaphore(5)
        self.mutex = Mutex()
        self.item_id = 0
        self.queue = []


def fnc_produce(shared):
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
    # process time


sh = Shared()
threads = []

# najprv sa zamerne vytvaraju vlakna pre spracoovanie vyrobkov
for i in range(10):
    threads.append(Thread(fnc_process, sh))
for i in range(10):
    threads.append(Thread(fnc_produce, sh))
for t in threads:
    t.join()
