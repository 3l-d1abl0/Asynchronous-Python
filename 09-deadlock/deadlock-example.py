from threading import Thread, Lock
import time

def red_robot(lock1, lock2):

    while True:
        print("RED: Acquiring lock 1")
        lock1.acquire()
        print("RED: Acquiring lock 2")
        lock2.acquire()

        print("RED: lock Acquired !")
        lock1.release()
        lock2.release()

        print("RED: Locks Released !\n")

        time.sleep(0.5)


def blue_robot(lock1, lock2):

    while True:
        print("BLUE: Acquiring lock 1")
        lock1.acquire()
        print("BLUE: Acquiring lock 2")
        lock2.acquire()

        print("BLUE: lock Acquired !")
        lock1.release()
        lock2.release()

        print("BLUE: Locks Released !\n")

        time.sleep(0.5)



if __name__ == "__main__":

    mutex1 = Lock()
    mutex2 = Lock()

    red = Thread(target=red_robot, args=(mutex1, mutex2,))
    blue = Thread(target=blue_robot, args=(mutex1, mutex2,))


    red.start()
    blue.start()