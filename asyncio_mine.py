import asyncio
from time import sleep


async def a_old():
    for i in range(10):
        print(i)

        sleep(1)


async def main_old():
    tasks=[]
    for arg in range(5):
        tasks.append(a_old())

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    results = asyncio.run(main_old())

#######

async def a():
    for i in range(10):
        print(i)

        await asyncio.sleep(1)


async def main():
    tasks=[]
    for arg in range(5):
        tasks.append(a())

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    results = asyncio.run(main())


#####
