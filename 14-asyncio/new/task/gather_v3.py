import asyncio

async def countdown(name, number):
    print(name, 'started')
    for i in range(number, 0, -1):
        print(name, i)
        await asyncio.sleep(1)

async def main():

    '''
    Passing coroutine to asyncio tasks directly
    it wont start running until it hits await asyncio
    '''
    tasks = [
        countdown('Task A', 2),
        countdown('Task B', 3),
        countdown('Task C', 2)
    ]
    await asyncio.sleep(3)
    print('Main done sleeping, about to await .gather')
    await asyncio.gather(*tasks)
    print('All done')

asyncio.run(main())
print('Outside of asyncio event loop')
