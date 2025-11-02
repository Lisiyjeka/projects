from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо дату народження з рядка у datetime.date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Формуємо дату дня народження у поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув цього року — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця між днем народження та сьогодні
        days_until_birthday = (birthday_this_year - today).days

        # Перевіряємо, чи день народження в межах наступних 7 днів (включно з сьогодні)
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            # Якщо день народження припадає на вихідні — переносимо на понеділок
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)

            # Додаємо до списку результатів
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.11.06"},
    {"name": "Alice Cooper", "birthday": "1995.11.04"}
]

upcoming = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming)