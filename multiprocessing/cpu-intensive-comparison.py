import time
import sys
from multiprocessing import Process, current_process

'''
    Using multithreading instead of using thread start and join
'''

def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def factorial(number):

    print ('Process : ', current_process().name, 'Starts')
    factorial = 1

    for n in range(1, number + 1):
        factorial *= n

    print ('Process : ', current_process().name, 'End \n')
    return factorial


if __name__ =="__main__":

    num_processes = int(sys.argv[1])
    processes = []
    number = 100000

    #serially
    factorial_of = number
    marker = time.time()
    for idx in range(num_processes):
        factorial(factorial_of)
        factorial_of +=1

    print("Time Taken : ", time.time() - marker,"\n")


    #Process
    marker = time.time()
    factorial_of = number
    #prepare the Processes
    for i in range(num_processes):
        process_name = "Process {}".format(i)
        p = Process(target=factorial, args=(factorial_of,), name=process_name)
        processes.append(p)
        p.start()
        factorial_of+=1

    for p in processes:
        p.join()

    print(f'{num_processes =} time={time.time()-marker} ')

    '''
    /usr/bin/python3 factorial.py 1
    /usr/bin/python3 factorial.py 2
    '''
