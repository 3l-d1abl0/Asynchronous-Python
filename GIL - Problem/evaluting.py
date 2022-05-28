import sys
from threading import Thread
from timeit import Timer
from urllib.request import Request, urlopen

class threads_object(Thread):
    def run(self):
        function_to_run()

class nothreads_object(object):
    def run(self):
        function_to_run()

def function_to_run():

    for i in range(10):
        
        req = Request("https://www.packtpub.com/", headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1'})
        with urlopen(req) as f:
            f.read()

def non_threaded(num_iter):

    funcs = []
    for i in range(int(num_iter)):
        funcs.append(nothreads_object())

    for i in funcs:
        i.run()


def threaded(num_threads):

    funcs = []
    
    for i in range(int(num_threads)):
        funcs.append(threads_object())
        
    for i in funcs:
        i.start()
            
    for i in funcs:
        i.join()

def show_results(func_name, results):

    print("%-23s %4.6f seconds" % (func_name, results))

if __name__ == "__main__":

    repeat = 5
    number = 1
    num_threads = [1, 2, 4, 8]
    
    print('Starting tests')
    
    for i in num_threads:
        
        t = Timer("non_threaded(%s)" % i, "from __main__ import non_threaded")
        best_result = min(t.repeat(repeat = repeat, number = number))
        show_results("non_threaded (%s iters)" % i, best_result)
        
        
        t = Timer("threaded(%s)" % i, "from __main__ import threaded")
        best_result = min(t.repeat(repeat = repeat, number = number))
        show_results("threaded (%s threads)" % i, best_result)
        
        print('Iterations complete')