import time
import threading
from concurrent.futures import ThreadPoolExecutor

'''
    Using multithreading instead of using thread start and join
'''

def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def factorial(x):

    print ('Thread #',x,' : ', threading.current_thread().name, 'Starts')
    number = 100000
    fac = 1

    for n in range(1, number + 1):
        fac *= n
    
    print ('Thread #',x,' : ', threading.current_thread().name, 'Ends \n')
    return fac



if __name__ =="__main__":

    number_of_threads = 4

    #Serially
    marker = time.time()
    for i in range(number_of_threads):
        factorial(i)

    print("Time Taken : ", time.time() - marker,"\n")


    #MultiThreading
    marker = time.time()
    multithreading(factorial, range(number_of_threads), number_of_threads)
    print("Time Taken : ", time.time() - marker)
