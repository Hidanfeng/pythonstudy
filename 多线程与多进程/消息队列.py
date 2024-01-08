from multiprocessing import Queue,Process,set_start_method

def task1(q):
    q.put('task')


def task2(q):
    print(q.get())


if __name__ == '__main__':
    set_start_method('fork')
    q = Queue()
    p1 = Process(target=task1,args=(q,))
    p2 = Process(target=task2,args=(q,))
    p1.start()
    p2.start()