from threading import Thread
from time import sleep
from multiprocessing import Process


def a():
    for i in range(10):
        print(i)
        sleep(1)


for i in range(5):
    th = Thread(target=a)
    th.start()


for i in range(5):
    if __name__ == "__main__":
        proc = Process(target=a)
        proc.start()
