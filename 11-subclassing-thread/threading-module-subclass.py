import threading
import time

exit_Flag = 0

class myThread (threading.Thread):

    
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter


    def run(self):
        print ("Starting " + self.name + "\n")
        print_time(self.name, self.counter, 5)
        print ("Exiting " + self.name + "\n")


def print_time(threadName, delay, counter):
    while counter:
        if exit_Flag:
            thread.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

#Main program
if __name__ == '__main__':


    # Create two threads
    thread1 = myThread(1, "Thread1", 1) #threadID counter name
    thread2 = myThread(2, "Thread2", 2) #threadID counter name

    # Start the Threads created
    thread1.start()
    thread2.start()

    # Wait for all thread to complete 
    thread1.join()
    thread2.join()

    print ("Exiting Main Thread")


