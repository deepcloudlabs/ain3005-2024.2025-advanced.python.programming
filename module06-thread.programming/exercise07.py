import asyncio


async def fun(numbers: list[int]) -> list[bool]:
    result: list[bool] = []
    for number in numbers:
        result.append(number % 2)
    return result


async def gun():
    return await asyncio.gather(
        fun(range(1, 10)),
        fun(range(10, 20)),
        fun(range(20, 30))
    )

async def application():
    solution = await gun()
    print(solution)


asyncio.run(application())