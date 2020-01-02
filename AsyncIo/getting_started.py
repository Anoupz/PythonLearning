import asyncio
import random


async def simple_co_routine():
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print("a simple example")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(simple_co_routine())
    loop.close()


main()
