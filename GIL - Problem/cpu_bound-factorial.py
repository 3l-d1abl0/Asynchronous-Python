from threading import Thread
import sys
import timeit


def calculate_factorial(number):
    factorial = 1

    for n in range(1, number + 1):
        factorial *= n

    return factorial


def calculate_factorial_using_threads(threads):
    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    number = 200000
    number_of_threads = int(sys.argv[1])
    threads = []
    
    for _ in range(number_of_threads):
        threads.append(Thread(target=calculate_factorial, args=(number,)))
        
    print(f'{timeit.timeit("calculate_factorial_using_threads(threads)", "from __main__ import calculate_factorial_using_threads, threads", number=1)}')

    '''
    /usr/bin/python3 factorial.py 1
    /usr/bin/python3 factorial.py 2
    '''
