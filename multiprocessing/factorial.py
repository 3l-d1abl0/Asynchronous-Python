from multiprocessing import Process
import time
import sys


def calculate_factorial(number):
    factorial = 1

    for n in range(1, number + 1):
        factorial *= n

    return factorial

if __name__ == "__main__":

    num_processes = int(sys.argv[1])
    processes = []
    number = 10000

    start = time.time()
    for i in range(num_processes):
        process_name = "Process {}".format(i)
        p = Process(target=calculate_factorial, args=(number,), name=process_name)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    end= time.time()
    print(f'{num_processes =} time={end-start} factorial of {number}')

    '''
    /usr/bin/python3 -m http.server 8000
    /usr/bin/python3 factorial.py 1
    /usr/bin/python3 factorial.py 2
    '''