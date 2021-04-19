import time
import asyncio
import aiohttp
import aiofiles


async def download_file(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.read()
    async with aiofiles.open(filename, "w+b") as outfile:
        await outfile.write(data)


async def main():
    start_time = time.perf_counter()
    await asyncio.gather(
        download_file('https://uim.fei.stuba.sk/wp-content/uploads/2018/02'
                      '/2021-07.iteracia-generator-korutina.pdf', 'file0.pdf'),
        download_file('https://uim.fei.stuba.sk/wp-content/uploads/2018/02'
                      '/2021-01.uvod-do-paralelnych-a-distribuovanych'
                      '-vypoctov.pdf', 'file1.pdf'),
        download_file('https://uim.fei.stuba.sk/wp-content/uploads/2018/02'
                      '/2021-04b.diningphilosophers.pdf', 'file2.pdf')
    )
    elapsed = time.perf_counter() - start_time
    print(f"\nTotal elapsed time: {elapsed:.1f} sec")

if __name__ == "__main__":
    asyncio.run(main())
