#!/usr/bin/python3

from threading import Thread, Condition
import time

items = []
condition = Condition()


class consumer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 0:
            print("Halting consumption ...")
            condition.wait()
            print("Resuming consumption ...")
        
        items.pop()
        print ('Consumer notify : consumed 1 item')
        print (f'Consumer notify : Remaining items {str(len(items))}')
        
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(5)
            self.consume()


class producer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 10:
            print("Halting production ...")
            condition.wait()
            print("Resuming production ...")
        
        items.append(1)
        print (f'Producer notify : Total items produced {str(len(items))}')
        
        condition.notify()
        condition.release()

    def run(self):
        
        for i in range(0, 20):
            time.sleep(2)
            self.produce()


if __name__ == '__main__':
    producer = producer()

    consumer = consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
