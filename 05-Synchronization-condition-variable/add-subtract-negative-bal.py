import time
from threading import Thread, Condition


class AddSubrtract:

    def __init__(self):
        self.cv = Condition()
        self.money = 1000

    def addNumber(self):

        for i in range(1000000):
            self.cv.acquire()
            self.money += 10
            self.cv.notify()
            self.cv.release()



    def subtractNumber(self):

        for _ in range(1000000):
            self.cv.acquire()
            while self.money < 10:
                self.cv.wait()
            self.money -= 10

            if self.money  <=0:
                print(f"Money in the Bank {self.money}")

            self.cv.release()
            


if __name__ == "__main__":

    obj = AddSubrtract()

    Thread(target=obj.addNumber, args=()).start()
    Thread(target=obj.subtractNumber, args=()).start()

    time.sleep(50)
    print(f"Money : {obj.money}")
