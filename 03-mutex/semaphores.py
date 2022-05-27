###Using a Semaphore to synchronize threads

import threading
import time
import random

#Default 1, if initalized less than zero -> valueError
semaphore = threading.Semaphore(0)

def consumer():
    print ("consumer is waiting.")
    ''' Acquire a semaphore
        this will as the value is 0 , until producer makes it 1 by releasing it
    '''
    semaphore.acquire()

    ##The consumer have access to the shared resource
    print ("Consumer notify : consumed item number %s " %item)


def producer():


    global item
    time.sleep(3)
    
    ##create a random item
    item = random.randint(0,1000)
    print ("producer notify : producted item number %s" %item)
    
    '''current value of semaphore 0, release will make it 1
        & consumer will start consuming
    '''
    semaphore.release()


if __name__ == '__main__':

    for i in range (0,1) :

        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
    
    print ("program terminated")

        

