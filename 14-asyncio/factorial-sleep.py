import asyncio
import time
from datetime import datetime


async def factorial_time_sleep(name:str , number: int):
    res =1
    for i in range(2, number+1):
        res *=i

        time.sleep(1)

    print(f"Taks {name}: factorial({number}) = {res}")




async def factorial_asyncio_sleep(name: str , number: int):
    res =1
    for i in range(2, number+1):
        res *=i

        await asyncio.sleep(1)

    print(f"Taks {name}: factorial({number}) = {res}")



if __name__=="__main__":

    #1. Using time

    start = time.time()
    

    '''tasks = [
        asyncio.ensure_future(factorial_time_sleep("A", 3)),
        asyncio.ensure_future(factorial_time_sleep("B", 4))
    ]'''

    #Get the event Loop
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(asyncio.wait(tasks))
    #loop.close()

    asyncio.run(factorial_time_sleep("A", 3))
    asyncio.run(factorial_time_sleep("B", 10))

    end = time.time()

    print(f"Time Taken : {end-start}")


    print("========================================")

    #2. For asyncio
    start = time.time()

    '''tasks = [
        asyncio.ensure_future(factorial_asyncio_sleep("A", 3)),
        asyncio.ensure_future(factorial_asyncio_sleep("B", 4))
    ]'''

    #Get the event Loop
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(asyncio.wait(tasks))
    #loop.close()
    asyncio.run(factorial_asyncio_sleep("A", 3))
    asyncio.run(factorial_asyncio_sleep("B", 10))

    end = time.time()

    print(f"Time Taken ASYNCIO : {end-start}")