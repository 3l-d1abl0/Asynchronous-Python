import random
import asyncio

async def is_prime_test(x):
    print('Processing: ', x)
    await asyncio.sleep(random.random())
    for i in range(2, x):
        if x % i == 0:
            return x, False
    return x, True



async def main():
    tasks = []
    for number in range(2, 100):
        tasks.append(asyncio.Task(is_prime_test(number)))
        
    #Returns the cumulative Result
    results = await asyncio.gather(*tasks)
    
    #The results are in Order even if the coroutines did not finish in that Order
    print(results)
    print('Primes: ')
    for x, is_prime in results:
        if is_prime:
            print(x, is_prime)

random.seed(42)
asyncio.run(main())