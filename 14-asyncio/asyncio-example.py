
import asyncio
import time
import aiohttp

async def download_site(session, url):

    print(loop.time())
    async with session.get(url) as response:
        #print(response.request_info)
        #print(dir(response))
        indicator = "J" if "jython" in url else "R"
        print(indicator, sep='', end='\n', flush=True)
    print(loop.time())



async def download_all_sites(sites):
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)

        #print(tasks)

        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':

    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    print("Starting downloads\n")
    start = time.time()
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_all_sites(sites))
    
    duration = time.time() - start
    print(f"\nDownloaded {len(sites)} sites in {duration} seconds")