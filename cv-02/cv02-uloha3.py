from fei.ppds import Thread, Semaphore, Event

FIBONACCI_NUMBER = 10  # fibonac. cislo, ktore chceme vypocitat
ADT = "semaphore"  # mozne zadat bud "event" alebo "semaphore"


class Shared():
    def __init__(self, size, adt):
        self.adt = adt
        self.size = size
        self.counter = 0
        self.fibonacci = list()
        self.fibonacci.append(0)
        self.fibonacci.append(1)
        if adt == "semaphore":
            self.semaphore = Semaphore(1)
        elif adt == "event":
            self.event = Event()


def fnc_fibonacci(shared):
    while True:
        if shared.adt == "semaphore":
            shared.semaphore.wait()
        elif shared.adt == "event":
            shared.event.clear()
        value = shared.counter
        shared.counter += 1
        if shared.adt == "semaphore":
            shared.semaphore.signal()
        elif shared.adt == "event":
            shared.event.signal()
        if value >= shared.size:
            break
        shared.fibonacci.append(shared.fibonacci[-1] + shared.fibonacci[-2])


shared = Shared(FIBONACCI_NUMBER-1, ADT)
threads = list()

for i in range(FIBONACCI_NUMBER-1):
    threads.append(Thread(fnc_fibonacci, shared))
for t in threads:
    t.join()

for x in range(len(shared.fibonacci)):
    print(shared.fibonacci[x])

# 1) Aký je najmenší počet synchronizačných objektov (semafory, mutexy, udalosti) potrebných na riešenie tejto úlohy?
# 1
# 2) Ktoré z prebratých synchronizačných vzorov sa dajú (rozumne) využiť pri riešení tejto úlohy?
# Vzajomne vylucenie; vo fcii fnc_fibonacci pristupuje k "shared.counter" vyzdy len 1 vlakno
