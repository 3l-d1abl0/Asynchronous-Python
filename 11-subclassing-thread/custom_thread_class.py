import threading
import time

class threadingClass(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):

        threading.Thread.__init__(self, group=group, target=target, name=name)

        self.args = args
        self.kwargs = kwargs
        return

    def run(self):

        curr_thread = threading.currentThread()
        time.sleep(1)
        print('running with %s and %s'%(self.args, self.kwargs))

        print(threading.current_thread().name)
        #print(curr_thread.getName())
        print(curr_thread.is_alive())
        

        return

if __name__ == "__main__":


    t = threadingClass(args=(1,), kwargs={'a': 'A', 'b':'B'})
    t.start()
