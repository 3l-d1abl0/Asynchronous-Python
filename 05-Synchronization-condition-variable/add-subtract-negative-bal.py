import time
from multiprocessing import Process, Lock

money = 1000
mutex = Lock()


class AddSubrtract:

    def addNumber(self):

        for i in range(1000000):
            mutex.acquire()
            global money
            money += 10
            mutex.release()
            print("+100")

        print("Done : addNumber")


    def subtractNumber(self):

        for _ in range(1000000):
            mutex.acquire()
            global money
            money -= 20
            if money <0:
                print(f"Money in the Bank {money}")
            mutex.release()
            print("-------------")

        print("Done : subtractNumber")


if __name__ == "__main__":

    obj = AddSubrtract()
    
    start = time.time()

    Process(target=obj.addNumber, args=()).start()
    Process(target=obj.subtractNumber, args=()).start()

    end = time.time()

    time.sleep(10)
    print(f"Money : {money}")
    print(f"Time Taken : {start-end}")
