"""
Кейс-задача №1. Стилистическое преобразование чисел (дата рождения).

Программа запрашивает у пользователя день, месяц и год рождения,
определяет день недели этой даты, проверяет год на високосность,
вычисляет текущий возраст пользователя и выводит дату рождения
в формате дд мм гггг, где цифры нарисованы звёздочками (*), как
на электронном табло.
"""

from datetime import date


# Шаблоны цифр 0-9 в виде "электронного табло" 5 строк x 3 столбца
DIGIT_PATTERNS = {
    '0': [" * ", "* *", "* *", "* *", " * "],
    '1': ["  *", "  *", "  *", "  *", "  *"],
    '2': ["***", "  *", "***", "*  ", "***"],
    '3': ["***", "  *", "***", "  *", "***"],
    '4': ["* *", "* *", "***", "  *", "  *"],
    '5': ["***", "*  ", "***", "  *", "***"],
    '6': ["***", "*  ", "***", "* *", "***"],
    '7': ["***", "  *", "  *", "  *", "  *"],
    '8': ["***", "* *", "***", "* *", "***"],
    '9': ["***", "* *", "***", "  *", "***"],
    '.': ["   ", "   ", "   ", "   ", " * "],
    ' ': ["   ", "   ", "   ", "   ", "   "],
}

WEEKDAYS = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "субботу",
    "воскресенье",
]


def get_birth_date():
    """Запрашивает у пользователя день, месяц и год рождения."""
    while True:
        try:
            day = int(input("Введите день рождения (1-31): "))
            month = int(input("Введите месяц рождения (1-12): "))
            year = int(input("Введите год рождения: "))
            # Проверка корректности введённой даты
            birth_date = date(year, month, day)
            return birth_date
        except ValueError as exc:
            print(f"Некорректная дата, попробуйте снова. ({exc})")


def get_weekday(birth_date: date) -> str:
    """Определяет день недели для заданной даты."""
    # weekday(): 0 - понедельник, 6 - воскресенье
    index = birth_date.weekday()
    return WEEKDAYS[index]


def is_leap_year(year: int) -> bool:
    """Определяет, является ли год високосным."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_age(birth_date: date) -> int:
    """Вычисляет текущий полный возраст пользователя в годах."""
    today = date.today()
    age = today.year - birth_date.year
    # Если день рождения в этом году ещё не наступил - вычитаем 1 год
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def render_scoreboard(text: str) -> str:
    """
    Возвращает строковое представление текста в виде электронного
    табло, где каждая цифра/символ нарисован звёздочками (*).
    """
    rows = ["" for _ in range(5)]
    for char in text:
        pattern = DIGIT_PATTERNS.get(char, DIGIT_PATTERNS[' '])
        for i in range(5):
            rows[i] += pattern[i] + "  "
    return "\n".join(rows)


def main():
    birth_date = get_birth_date()

    weekday = get_weekday(birth_date)
    print(f"\nВы родились в {weekday}.")

    leap = is_leap_year(birth_date.year)
    print(f"Год {birth_date.year} {'високосный' if leap else 'не високосный'}.")

    age = get_age(birth_date)
    print(f"Сейчас вам {age} лет.")

    # Формат дд мм гггг
    date_string = f"{birth_date.day:02d}.{birth_date.month:02d}.{birth_date.year}"
    print("\nВаша дата рождения на электронном табло:\n")
    print(render_scoreboard(date_string))


if __name__ == "__main__":
    main()
