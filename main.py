import multiprocessing as mp
import time
import random
import keyboard as kb


def maker(q):
    sleeping = True
    while(True):
        #print(sleeping)
        if sleeping:
            if q.qsize() < 80:
                sleeping = False
        else:
            if q.qsize() > 200:
                sleeping = True
        if not sleeping:
            q.put(random.randint(1, 100))
        time.sleep(0.1)


def consumer(q):
    while(True):
        if not q.empty():
            print(q.get(), q.qsize())
            pass
        time.sleep(0.1)


if __name__ == "__main__":
    random.seed()

    queue = mp.Queue()

    NUM_MAKERS = 3
    NUM_CONSUMERS = 2

    makers = []
    consumers = []
    for _ in range(NUM_MAKERS):
        p = mp.Process(target=maker, args=(queue,))
        makers.append(p)
        p.start()
    for _ in range(NUM_CONSUMERS):
        p = mp.Process(target=consumer, args=(queue,))
        consumers.append(p)
        p.start()

    kb.wait('q')
    for x in makers:
        x.terminate()
    while queue.qsize() > 0:
        time.sleep(1)
    for x in consumers:
        x.terminate()
