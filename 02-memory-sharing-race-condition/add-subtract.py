import time
from multiprocessing import Process

class AddSubrtract:

    money = 1000



    def addNumber(self):
        for i in range(1000000):
            self.money += 10
            print("+100")

        print("Done : addNumber")


    def subtractNumber(self):

        for _ in range(1000000):
            self.money -= 10
            print("-------------")

        print("Done : subtractNumber")


if __name__ == "__main__":

    obj = AddSubrtract()
    
    start = time.time()

    Process(target=obj.addNumber, args=()).start()
    Process(target=obj.subtractNumber, args=()).start()

    end = time.time()

    time.sleep(5)
    print(f"Money : {obj.money}")
    print(f"Time Taken : {start-end}")
