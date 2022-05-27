from threading import Thread, Event
from queue import Queue
import time
import random


class producer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print (f'Producer notify : item N° {item} appended to queue by {self.name} \n')
            time.sleep(1)


class consumer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):

        while True:
            item = self.queue.get()
            print ('Consumer notify : {item} popped from queue by {self.name}')
            self.queue.task_done()


if __name__ == '__main__':


        queue = Queue()
        
        t1 = producer(queue)
        t2 = consumer(queue)
        t3 = consumer(queue)
        
        t1.start()
        t2.start()
        t3.start()
        
        t1.join()
        t2.join()
        t3.join()