import time
from queue import Queue
from threading import Thread

def consumer(q):

    while(True):
        txt  = q.get()
        print("Received : ",txt)
        time.sleep(1)


def producer(q):

    msg = "Message "
    ctr = 1
    while(True):

        q.put(msg+str(ctr))
        print("Message Sent "+msg+str(ctr))
        ctr+=1
        time.sleep(1)


if __name__ == "__main__":

    q = Queue()

    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))


    t1.start()
    t2.start()