from current_lesson import *
from datetime import *


def m_response(dic) -> str:
    # удалить позже
    dic["день_недели"] = 0 # для отладки понедельник

    # читаем все расписание
    shed = read_schedule_file()
    # оставляем только расписание указанного класса
    shed = shed[shed.find(dic["класс"]) + 1:]
    shed = shed[shed.find("\n") + 1:]
    answer = "---"
    if dic["следующий"] == 1:
        answer = next_lesson(dic, shed)  # следующий урок (следующий)
    elif dic["вся_неделя"] == 1:
        answer = "-" #all_week(dic, shed) # вся неделя (неделя)
    else:
        answer = shed_for_day(dic, shed)

    if dic["осталось"] == 1:
        answer = answer + " " + remaind(dic, shed)  # осталось до конца урока (.)
        dic["осталось"] = 0

    return answer


def next_lesson(dic, shed) -> str:
    lesson = cur_lesson() + 1
    text = shed[shed.find("w" + str(dic["день_недели"])) + 3:]
    text = text[text.find(str(lesson)) + 2:]
    text = text[:text.find("\n")]

    return text


def remaind(dic, shed) -> str:
    now = datetime.today()
    minutes = int(now.strftime("%H")) * 60 + int(now.strftime("%M"))

# 100

    if minutes < 8 * 60 + 20:
        time_left = "Уроки еще не начались"
    elif minutes < 8 * 60 + 55:     # 08:55 окончание 0 урока
        time_left = "Осталось " + str(8 * 60 + 55 - minutes) + " минут"
    elif minutes <= 9 * 60 + 00:  # 09:45 окончание 1 урока
        time_left = "Осталось " + str(9 * 60 + 00 - minutes) + " минут"
    elif minutes <= 9 * 60 + 55:  # 10:40 окончание 2 урока
        time_left = "Осталось " + str(9 * 60 + 55 - minutes) + " минут"
    elif minutes <= 10 * 60 + 45:  # 11:45 окончание 3 урока
        time_left = "Осталось " + str(10 * 60 + 45 - minutes) + " минут"
    elif minutes <= 11 * 60 + 50:  # 12:50 окончание 4 урока
        time_left = "Осталось " + str(11 * 60 + 50 - minutes) + " минут"
    elif minutes <= 12 * 60 + 55:  # 13:55 окончание 5 урока
        time_left = "Осталось " + str(12 * 60 + 55 - minutes) + " минут"
    elif minutes <= 13 * 60 + 55:  # 14:55 окончание 6 урока
        time_left = "Осталось " + str(13 * 60 + 55 - minutes) + " минут"
    else:
        time_left = "Уроки на сегодня кончились"  # "Уроки на сегодня кончились"

    print(f"До конца урока осталось: {time_left}")

    return time_left


def shed_for_day(dic, shed) -> str:
    text = shed[shed.find("w" + str(dic["день_недели"])) + 3:]
    text = text[:text.find("w")]
    return text


def help() -> str:
    text = ("как использовать бот\n"
            "ключ - что делает\n"
            "9 - выдать расписание всех 9 классов на сегодня\n"
            "9А - выдать расписание класса на сегодня\n"
            "9А следующий - выдать следующий урок 9А\n"
            "9А понедельник - выдать расписание класса на понедельник\n"
            "понедельник 9А - - выдать расписание класса на понедельник\n"
            "9A. - сколько осталось до конца урока\n")
    return text


def read_schedule_file() -> str:
    file = open("расписание.txt", encoding='utf-8')
    # shed - schedule (расписание)
    shed = file.read()
    check_file_for_eng_letters(shed)
    return shed


def check_file_for_eng_letters(shed):
    alphabet = set('abcdefghijklmnopqrstuvxyz')
    line = 1
    for sym in shed:
        if sym == '\n':
            line += 1
        if not alphabet.isdisjoint(sym.lower()):
            print("Ошибка! В файле с расписанием обнаружены английские буквы на строке", line, "символ:", sym)
