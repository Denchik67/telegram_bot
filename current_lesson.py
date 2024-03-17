import datetime

# current_lesson функция определяет текущий урок и возвращает число, номер урока
# ответ 8 означает "Уроки на сегодня кончились"
# ответ -1 означает "Уроки не начались"
def cur_lesson() -> int:
    now = datetime.datetime.today()
    minutes = int(now.strftime("%H")) * 60 + int(now.strftime("%M"))

    if minutes < 8 * 60 + 20:
        current_lesson = -1  # "Уроки не начались"
    elif minutes <= 9 * 60 + 00:
        current_lesson = 0
    elif minutes <= 9 * 60 + 55:
        current_lesson = 1
    elif minutes <= 10 * 60 + 45:
        current_lesson = 2
    elif minutes <= 11 * 60 + 50:
        current_lesson = 3
    elif minutes <= 12 * 60 + 55:
        current_lesson = 4
    elif minutes <= 13 * 60 + 55:
        current_lesson = 5
    elif minutes <= 14 * 60 + 55:
        current_lesson = 6
    elif minutes <= 15 * 60 + 45:
        current_lesson = 7
    else:
        current_lesson = 8  # "Уроки на сегодня кончились"

    return current_lesson


def current_time() -> str:
    now = datetime.datetime.today()
    return now.strftime("%H:%M:%S")


def current_day() -> int:
    now = datetime.datetime.today()
    return now.weekday()

