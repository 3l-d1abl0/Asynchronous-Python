import asyncio


async def main():

    print("Hello")
    await asyncio.sleep(2)
    print("World")


if __name__ == "__main__":

    #Type Coroutine
    print(type(main))

    asyncio.run(main())