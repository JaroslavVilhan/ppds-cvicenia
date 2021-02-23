from fei.ppds import Thread, Mutex
import numpy


class Shared():
    def __init__(self, end):
        self.counter = 0
        self.end = end
        self.elms = [0] * end
        self.mutex = Mutex()


# Kedze pri prepinani medzi vlaknami je tazke ustrazit hodnotu premennej counter, riesenie by islo cez aktulane
# vytvorenu lokalnu premennu v beziacom vlakne - cize kazde vlakno si vytvori takuto premennu a ked dojde k prepnutiu
# medzi vlaknami, kazde si tu svoju zapamata a s nasledujucou castou programu pracuje s planovanou hodnotou.
# Samozrejme "shared.counter += 1" tiez musi patrit do kritickej oblasti, aby sa zabranilo moznej viacnasobnej
# inkrementacie
def fnc_test(shared):
    while True:
        shared.mutex.lock()
        value = shared.counter
        shared.counter += 1
        shared.mutex.unlock()
        if value >= shared.end:
            break
        shared.elms[value] += 1


shared = Shared(1_000_000)
t1 = Thread(fnc_test, shared)
t2 = Thread(fnc_test, shared)
t1.join()
t2.join()

# vypis pocetnosti prvkov nachadzajucich sa v zdielanom poli
print(numpy.array(numpy.unique(shared.elms, return_counts=True)).T)
