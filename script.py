import aiohttp
import asyncio

cities_for_check = ['Лондон', 'Шереметьево', 'Череповец']
weather_url = 'https://ru.wttr.in'
params = '?M?n?q?T'


async def get_weather_for_city(cities):
    async with aiohttp.ClientSession() as session:
        for city in cities:
            request = f'{weather_url}/{city}{params}'

            async with session.get(request) as resp:
                city_weather = await resp.text()
                print(city_weather)


if __name__ == '__main__':
    asyncio.run(get_weather_for_city(cities_for_check))
