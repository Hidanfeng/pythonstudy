import asyncio

async def func():
    print('hh')
    return 10

result = func()
print(result)
asyncio.run(result)

#await