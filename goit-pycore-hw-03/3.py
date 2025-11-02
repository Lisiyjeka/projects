import re

def normalize_phone(phone_number: str) -> str:
    # Видаляємо зайві пробіли на початку та в кінці
    phone_number = phone_number.strip()

    # Видаляємо всі символи, крім цифр та '+'
    phone_number = re.sub(r"[^\d+]", "", phone_number)

   # Форматуємо номер відповідно до правил
    if phone_number.startswith("+380"):
        # Повний український номер
        return phone_number
    elif phone_number.startswith("+38"):
        # Неповний український номер (наприклад, +38501234567)
        # Перетворюємо на повний: +380501234567
        return "+380" + phone_number[3:]
    elif phone_number.startswith("380"):
        # Номер з кодом 380 без +
        return "+" + phone_number
    elif phone_number.startswith("+"):
        # Інші міжнародні номери
        return phone_number
    else:
        # Локальний номер
        return "+38" + phone_number
# дані для тестування
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+389 44 123 4567"

]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)