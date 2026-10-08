import asyncio


async def countdown(name, seconds):
    """
    Асинхронная функция-таймер.
    Принимает имя таймера (name) и количество секунд (seconds).
    Печатает числа от seconds до 1 с паузой в 1 секунду,
    а затем выводит сообщение о пуске.
    """
    # Цикл от seconds до 1 включительно (шаг -1)
    for i in range(seconds, 0, -1):
        print(i)
        # Асинхронная пауза на 1 секунду
        await asyncio.sleep(1)

    # Вывод сообщения после завершения отсчета
    print(f"{name}: Пуск!")
async def main():
    # Пример вызова из задания
    await countdown("Таймер 1", 3)


if __name__ == "__main__":
    # Запуск асинхронной программы
    asyncio.run(main())
