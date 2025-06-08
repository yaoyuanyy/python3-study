# asyncio 是 python 异步编程的基础
import asyncio


async def hello(name):
    print("hello %s" % name)
    await asyncio.sleep(1)
    print('hello %s again' % name)
    return name


async def main():
    tasks = [hello('a'), hello('b')]
    results = await asyncio.gather(*tasks)
    print('result:', results)


asyncio.run(main(), debug=True)
