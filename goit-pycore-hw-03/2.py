import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка валідності параметрів
    if (
        min_num < 1 or 
        max_num > 1000 or 
        quantity < 1 or 
        quantity > (max_num - min_num + 1) or 
        min_num > max_num
    ):
        return []  # Повертаємо порожній список, якщо параметри некоректні

    # Генеруємо унікальні випадкові числа
    numbers = random.sample(range(min_num, max_num + 1), quantity)

    # Сортуємо список
    numbers.sort()
    return numbers


#  використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("виграшні  числа:", lottery_numbers)