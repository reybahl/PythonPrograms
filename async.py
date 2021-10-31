import asyncio
import time
async def printer():
    print('starting')
    for x in range(10):
        print('hello')

async def timer():
    print("h")
    await asyncio.sleep(5)

async def main():
    await asyncio.gather(timer(), timer())

    # asyncio.gather(timer(),timer(), timer())

async def speak_async():
    print('Asynchronicity!')
    asyncio.sleep(5)
    print("bye")

# loop.run(speak_async())
# loop.close()
# print('hello')
asyncio.run(main())