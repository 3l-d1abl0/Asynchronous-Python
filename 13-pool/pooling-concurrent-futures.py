#!/usr/bin/python3
# -*- coding: utf-8 -*-
##Concurrent.Futures Pooling - Section 4 Asynchronous Programming

import concurrent.futures
import time

number_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    ]


def evaluate_item(x):

    # count...just to make an operation

    for i in range(0, 10000000):
        i = i + 1

    # print the input item and the result

    print (f'item {str(x)}  result {str(i*x)}')


if __name__ == '__main__':

    # #Sequential Execution
    start_time = time.time()
    for item in number_list:
        evaluate_item(item)

    print (f'Sequential execution : {str(time.time() - start_time)} seconds\n')


    print("---------------------------------------------")


    # #Thread pool Execution
    start_time_1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

        for item in number_list:
            executor.submit(evaluate_item, item)

    print (f'Thread pool execution : {str(time.time() - start_time_1)} seconds\n')

    print("---------------------------------------------")

    # #Process pool Execution
    start_time_2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        
        for item in number_list:
            executor.submit(evaluate_item, item)
    
    print (f'Process pool execution : {str(time.time() - start_time_2)} seconds')
