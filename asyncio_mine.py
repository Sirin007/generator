"""как принято: импортировать пакет или нужные функции.
насколько тяжела операция импорта, стоит ли об этом думать
Typo: In word htmls
pip3 install certifi
open /Applications/Python\ 3.9/Install\ Certificates.command

aiohttp.client_exceptions.ClientConnectorCertificateError:
Cannot connect to host pokeapi.co:443 ssl:True [SSLCertVerificationError:
(1, '[SSL: CERTIFICATE_VERIFY_FAILED]
certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')]"""

import asyncio
# import requests
import aiohttp
from time import sleep


"""
async def a_old():
    for i in range(10):
        print(i)

        sleep(1)


async def main_old():
    tasks = []
    for arg in range(5):
        tasks.append(a_old())

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    results = asyncio.run(main_old())


async def a():
    for i in range(10):
        print(i)

        await asyncio.sleep(1)


async def main():
    tasks = []
    for arg in range(5):
        tasks.append(a())

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    results = asyncio.run(main())
"""


async def load_get(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main_response():
    urls = ['https://reg.olimpiada.ru/',
            'https://www.facebook.com/',
            'https://yandex.ru/?clid=2453500',
            'https://vk.com/im',
            'https://www.youtube.com/'
            ]
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(load_get(session, url))
        htmls = await asyncio.gather(*tasks)
        htmls_sort = sorted(htmls)
        for x in htmls_sort:
            print(len(x))


if __name__ == '__main__':
    results = asyncio.run(main_response())
