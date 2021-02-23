from fei.ppds import Thread, Mutex
import numpy


class Shared():
    def __init__(self, end):
        self.counter = 0
        self.end = end
        self.elms = [0] * end
        self.mutex = Mutex()


# Pri tomto rieseni moze nastat nasledovna situacia:
# 1.) plati, ze aktualna hodnota counteru ma velkost end-1.
# 2.) vlakno, ktore ide inkrementovat couter zamkne tuto oblast - nasledne counter inkrementuje, ale tesne pred
# odomknutim planovac preda riadenie druhemu vlaknu, ktore uz skontrolovalo podmienku (vyhodnotilo ju ako FALSE,
# kedze este predtym bola hodnota counteru end-1) a pokracuje dalej vo vykonavani.
# 3.) Vlakno pokracuje vo vykonavani kodu "shared.elms[shared.counter] += 1" vstupy do pola cez prekroceny index a
# sposobi chybne spravanie programu.
def fnc_test(shared):
    while True:
        if shared.counter >= shared.end:
            break
        shared.elms[shared.counter] += 1
        shared.mutex.lock()
        shared.counter += 1
        shared.mutex.unlock()


shared = Shared(1_000_000)
t1 = Thread(fnc_test, shared)
t2 = Thread(fnc_test, shared)
t1.join()
t2.join()

# vypis pocetnosti prvkov nachadzajucich sa v zdielanom poli
print(numpy.array(numpy.unique(shared.elms, return_counts=True)).T)
