import random
import string


def generate_password(length, use_lower, use_upper, use_digits, use_punctuation):
    """
    Генерирует надежный пароль с гарантированным включением
    хотя бы одного символа каждого выбранного типа.
    """
    # Собираем пулы символов на основе выбора пользователя
    # Модуль string избавляет от необходимости писать алфавиты вручную
    lower_pool = string.ascii_lowercase if use_lower else ""
    upper_pool = string.ascii_uppercase if use_upper else ""
    digits_pool = string.digits if use_digits else ""
    punct_pool = string.punctuation if use_punctuation else ""

    # Объединяем все разрешенные символы в один список для заполнения остатка
    all_allowed_chars = lower_pool + upper_pool + digits_pool + punct_pool

    # Подсчитываем, сколько типов символов выбрано
    selected_types_count = sum([bool(lower_pool), bool(upper_pool), bool(digits_pool), bool(punct_pool)])

    # --- ПРОВЕРКИ (Обработка крайних случаев) ---
    if not all_allowed_chars:
        return "Ошибка: Вы не выбрали ни одного типа символов."

    if length < selected_types_count:
        return (f"Ошибка: Длина пароля слишком мала. Чтобы гарантированно включить "
                f"все {selected_types_count} выбранных типа(ов) символов, "
                f"длина должна быть не менее {selected_types_count}.")

    # --- ГЕНЕРАЦИЯ ---
    password_chars = []

    # 1. Гарантированно добавляем по одному символу из каждого выбранного типа (Совет из текста)
    if use_lower:
        password_chars.append(random.choice(lower_pool))
    if use_upper:
        password_chars.append(random.choice(upper_pool))
    if use_digits:
        password_chars.append(random.choice(digits_pool))
    if use_punctuation:
        password_chars.append(random.choice(punct_pool))

    # 2. Заполняем оставшуюся длину случайными символами из общего пула
    remaining_length = length - len(password_chars)
    if remaining_length > 0:
        password_chars.extend(random.choices(all_allowed_chars, k=remaining_length))

    # 3. Перемешиваем символы (random.shuffle), чтобы гарантированные символы
    # не стояли всегда в начале пароля
    random.shuffle(password_chars)

    # Превращаем список обратно в строку
    return "".join(password_chars)


def main():
    """Консольный интерфейс программы."""
    print("=" * 40)
    print("🔐 Генератор надежных паролей")
    print("=" * 40)

    try:
        length = int(input("Введите желаемую длину пароля (целое число): "))
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")
        return

    print("\nВыберите типы символов для включения (y/n):")
    use_lower = input("Строчные буквы (abc...)? (y/n): ").strip().lower() == 'y'
    use_upper = input("Заглавные буквы (ABC...)? (y/n): ").strip().lower() == 'y'
    use_digits = input("Цифры (123...)? (y/n): ").strip().lower() == 'y'
    use_punct = input("Спецсимволы (!@#...)? (y/n): ").strip().lower() == 'y'

    # Вызов функции генерации
    password = generate_password(length, use_lower, use_upper, use_digits, use_punct)

    print("\n" + "-" * 40)
    print(f"Ваш сгенерированный пароль: \n{password}")
    print("-" * 40)


if __name__ == "__main__":
    main()