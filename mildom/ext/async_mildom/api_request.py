import aiohttp
import asyncio
import async_timeout

async def main():
    pass

async def request(url):
    async def get(url):
        if request_type == 'get':
            async with aiohttp.ClientSession() as session:
                body = await fetch(session, url, None, 'get')
                return body
        if headers is None:
            async with aiohttp.ClientSession() as session:
                body = await fetch(session, url, data, request_type)
                return body
        else:
            async with aiohttp.ClientSession(headers=headers) as session:
                body = await fetch(session, url, data, request_type)
                return body


async def fetch(session, url, data, request_type):
    with async_timeout.timeout(10):
        # database read API
        if request_type == 'get':
            async with session.get(url) as response:
                response_content = await response.read()
                if response.status != 200:
                    raise ConnectionError(f'url:{url}, response:{response_content.decode()}')
                return response_content
        # database write API
        elif type(data) == dict:
            async with session.post(url, json=data) as response:
                response_content = await response.read()
                if response.status != 200:
                    raise ConnectionError(f'url:{url}, data:{data}, response:{response_content.decode()}')
                return response_content
        # Google TTS
        else:
            async with session.post(url, data=data) as response:
                response_content = await response.read()
                if response.status != 200:
                    raise ConnectionError(f'url:{url}, data:{data}, response:{response_content.decode()}')
                return response_content


if __name__ == '__main__':
    loop = asyncio.get_running_loop()
    if loop is None:
        loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
