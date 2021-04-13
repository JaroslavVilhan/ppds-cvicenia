class Planovac():
    def __init__(self, tasks):
        self.tasks = tasks
        self.status = 'ok'

    def spusti_task(self, task):
        try:
            task[1].send(None)
        except StopIteration:
            print("PLANOVAC -- task " + task[0] + " skoncil...")
            self.tasks.remove(task)

    def spusti_planovac(self):
        while True:
            if tasks:
                for task in tasks:
                    self.spusti_task(task)
            else:
                print("PLANOVAC -- ziadne dalsie tasky !")
                self.status = 'ziadne-tasky'
                break

    def pridaj_dalsi_task(self, task):
        self.tasks.append(task)

    def ukonci_task(self, name):
        for task in tasks:
            if task[0] == name:
                print("PLANOVAC -- ukoncujem task " + name + "...")
                task[1].close()
                self.tasks.remove(task)


def task_a():
    count = 0
    while True:
        count += 1
        print("Hello from Task A ! x" + str(count))
        if count > 10:
            print("Task A -- Koncim !")
            break
        yield


def task_b():
    count = 0
    while True:
        count += 1
        print("Hello from Task B ! x" + str(count))
        if count > 5:
            print("Task B -- Koncim !")
            break
        if count == 2:
            print("Task B -- Idem ukoncit Task A !!!")
            planovac.ukonci_task('a')
        yield


def task_c():
    count = 0
    while True:
        count += 1
        print("Hello from Task C ! x" + str(count))
        if count > 3:
            print("Task C -- Koncim !")
            break
        yield


def task_d():
    count = 0
    while True:
        count += 1
        print("Hello from Task D ! x" + str(count))
        if count > 2:
            print("Task D -- Koncim !")
            break
        yield


tasks = [['a', task_a()], ['b', task_b()], ['c', task_c()]]

planovac = Planovac(tasks)
planovac.spusti_planovac()

if planovac.status == 'ziadne-tasky':
    planovac.pridaj_dalsi_task(['d', task_d()])
    planovac.spusti_planovac()
