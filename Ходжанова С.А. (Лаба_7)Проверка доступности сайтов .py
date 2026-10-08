import asyncio
import aiohttp


async def check_status(session, url):
    """
    Асинхронная корутина для проверки статуса одного веб-сайта.
    Принимает сессию aiohttp и URL.
    """
    try:
        # Выполняем GET-запрос с помощью aiohttp
        async with session.get(url) as response:
            # Проверяем код ответа
            if response.status == 200:
                return f"{url}: ОК"
            else:
                return f"{url}: Ошибка {response.status}"

    except aiohttp.ClientError:
        # Ловим ошибки соединения (например, несуществующий домен)
        return f"{url}: Не удалось подключиться"
    except asyncio.TimeoutError:
        # Ловим ошибки таймаута (если сайт слишком долго не отвечает)
        return f"{url}: Не удалось подключиться (превышено время ожидания)"
    except Exception as e:
        # Ловим любые другие непредвиденные ошибки
        return f"{url}: Не удалось подключиться ({e})"


async def main():
    # 1. Список URL-адресов из задания
    urls = [
        'https://www.python.org',
        'https://www.google.com',
        'https://non-existent-domain-12345.org'
    ]

    # 5. Используем asyncio.gather для одновременной проверки всех сайтов
    # Создаем одну сессию для всех запросов (это эффективнее, чем открывать новую для каждого)
    async with aiohttp.ClientSession() as session:
        # Создаем список задач (корутин)
        tasks = [check_status(session, url) for url in urls]

        # Запускаем все задачи одновременно и ждем их завершения
        results = await asyncio.gather(*tasks)

        # Выводим результаты на экран
        for result in results:
            print(result)


if __name__ == "__main__":
    # Запуск асинхронной программы
    asyncio.run(main())