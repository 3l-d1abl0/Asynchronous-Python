import time
from multiprocessing import Process, Queue

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

    p1 = Process(target=consumer, args=(q,))
    p2 = Process(target=producer, args=(q,))


    p1.start()
    p2.start()