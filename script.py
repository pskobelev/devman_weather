import aiohttp
import asyncio

cities_for_check = ['Лондон', 'Шереметьево', 'Череповец']
weather_url = 'https://ru.wttr.in'
payload = {'M': '', 'n': '', 'q': '', 'T': ''}


async def get_weather_for_city(cities):
    async with aiohttp.ClientSession() as session:
        for city in cities:
            request = f'{weather_url}/{city}'
            async with session.get(request, params=payload) as resp:
                try:
                    resp.raise_for_status()
                except aiohttp.ClientResponseError as e:
                    print(f"HTTP error: {e.status}")
                else:
                    city_weather = await resp.text()
                    print(city_weather)


if __name__ == '__main__':
    asyncio.run(get_weather_for_city(cities_for_check))
