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


tasks = [['a', task_a()], ['b', task_b()], ['c', task_c()]]
