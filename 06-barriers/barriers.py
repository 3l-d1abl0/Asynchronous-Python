import time

from threading import Barrier, Thread


barrier = Barrier(2)


def wait_on_barrier(name, time_to_sleep):

    for i in range(10):

        print(name, "running")
        time.sleep(time_to_sleep)
        print(name, "is waiting on barrier ",i)
        barrier.wait()
    
    print(name, "is finished")



if __name__ == "__main__":


    red = Thread(target=wait_on_barrier, args=["red", 2])
    blue = Thread(target=wait_on_barrier, args=["blue", 4])

    red.start()
    blue.start()