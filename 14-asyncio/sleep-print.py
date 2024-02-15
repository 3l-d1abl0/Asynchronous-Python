import asyncio
from datetime import datetime
import click


async def sleep_and_print(seconds):
    loop = asyncio.get_running_loop()
    print(f"starting async {seconds} sleep 😴", f"{loop.time()}")
    await asyncio.sleep(seconds)
    print(f"finished async {seconds} sleep ⏰", f"{loop.time()}")
    return seconds


async def main():
    # using arguments
    '''
    gather takes variable length of awaitables and schedule them as tasks
    '''
    results = await asyncio.gather(sleep_and_print(3), sleep_and_print(6))

    # building list
    # coroutines_list = []
    # for i in range(1, 11):
    #     coroutines_list.append(sleep_and_print(i))
    # results = await asyncio.gather(*coroutines_list)
    print(results)


start = datetime.now()

'''
Run is higher level API
run method expects a coroutine object
'''
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")