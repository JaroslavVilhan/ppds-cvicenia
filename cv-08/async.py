import aiohttp
import aiofiles


async def download_file(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.read()
    async with aiofiles.open(filename, "w+b") as outfile:
        await outfile.write(data)
