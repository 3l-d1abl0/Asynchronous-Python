from threading import *
import time


def job1():
    print(f"{current_thread().name}, Daemon: :{current_thread().daemon}")

    t = Thread(target=job2, name='New Child Thread')
    t.start()


def job2():
    print(f"{current_thread().name}, Daemon? :{current_thread().daemon}")
    print(f"{active_count()}")

if __name__ == "__main__":

    t = Thread(target=job1, name='Child Thread')
    t.daemon = True
    t.start()
    time.sleep(10)
    print(f"{active_count()}")