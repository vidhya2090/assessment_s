import asyncio
import aiohttp
import time


async def health_check(services_addresses):
    print("starting of the function ")
    await asyncio.sleep(0.5)
    health_services = {}
    async with aiohttp.ClientSession() as session:
        for address in services_addresses:
            start_time = time.time()
            async with session.get('http://127.0.0.1:8000/firstapp/home/') as response:
                end_time = time.time()
                response_time = end_time - start_time
                if response.status == 200 and response_time < 0.5:
                    health_services[address] = True
                else:
                    health_services[address] = False
    print(health_services)
    print("Ending of the function ")
    return health_services

async def main():
    data = [['http://127.0.0.1:8000/firstapp/home/', 'http://127.0.0.1:8000/firstapp/profile'],['http://127.0.0.1:8000/firstapp/home/'],['http://127.0.0.1:8000/firstapp/home/', 'http://127.0.0.1:8000/firstapp/profile']]
    coros= [health_check(i) for i in data]
    await asyncio.gather(*coros)


if __name__ == '__main__':
    asyncio.run(main())
