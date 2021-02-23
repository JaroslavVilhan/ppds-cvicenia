from fei.ppds import Thread, Mutex
import numpy


class Shared():
    def __init__(self, end):
        self.counter = 0
        self.end = end
        self.elms = [0] * end
        self.mutex = Mutex()


# Pri tomto rieseni moze nastat nasledovna situacia:
# Vlakno, ktore ma predane riadenie od planovaca zacne vykonavat cyklus while a nasledne uzamkne oblast celeho tela
# cyklu. Planovac sa rozhodne predat riadenie druhemu vlaknu, ktore sa tiez chysta vykonavat cyklus while. Kedze ho ale
# prve vlakno zamklo nastane uviaznutie.
def fnc_test(shared):
    while True:
        shared.mutex.lock()
        if shared.counter >= shared.end:
            break
        shared.elms[shared.counter] += 1
        shared.counter += 1
        shared.mutex.unlock()


shared = Shared(1_000_000)
t1 = Thread(fnc_test, shared)
t2 = Thread(fnc_test, shared)
t1.join()
t2.join()

# vypis pocetnosti prvkov nachadzajucich sa v zdielanom poli
print(numpy.array(numpy.unique(shared.elms, return_counts=True)).T)
