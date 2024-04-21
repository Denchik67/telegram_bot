from current_lesson import *
from datetime import *


def m_response(dic) -> str:
    # удалить позже
    #dic["день_недели"] = 3  # для отладки понедельник

    # читаем все расписание
    shed = read_schedule_file()
    # оставляем только расписание указанного класса
    shed = shed[shed.find(dic["класс"]) + 1:]
    shed = shed[shed.find("\n") + 1:]
    shed = shed[:shed.find("\n\n")]

    answer = "---"
    if dic["следующий"] == 1:
        dic["следующий"] = 0
        answer = next_lesson(dic, shed)  # следующий урок (следующий)
    elif dic["вся_неделя"] == 1:
        dic["вся_неделя"] = 0
        answer = all_week(dic, shed)  # вся неделя (неделя)
    else:
        answer = shed_for_day(dic, shed)

    if dic["осталось"] == 1:
        dic["осталось"] = 0
        answer = answer + " " + remaind(dic, shed)  # осталось до конца урока (.)

    return answer


def next_lesson(dic, shed) -> str:
    lesson = cur_lesson() + 1
    text = shed[shed.find("w" + str(dic["день_недели"])) + 3:]
    text = text[text.find(str(lesson)) + 2:]
    text = text[:text.find("\n")]

    return text


def all_week(dic, shed) -> str:
    shed = shed.replace("w0", "\nПОНЕДЕЛЬНИК")
    shed = shed.replace("w1", "\nВТОРНИК")
    shed = shed.replace("w2", "\nСРЕДА")
    shed = shed.replace("w3", "\nЧЕТВЕРГ")
    shed = shed.replace("w4", "\nПЯТНИЦА")
    shed = shed.replace("w5", "\nСУББОТА")
    shed = shed.replace("w6", "\nВОСКРЕСЕНЬЕ")
    shed = shed[:-1]
    return shed


def remaind(dic, shed) -> str:
    now = datetime.today()
    minutes = int(now.strftime("%H")) * 60 + int(now.strftime("%M"))

    # 100

    if minutes < 8 * 60 + 55:
        time_left = "Уроки еще не начались"
    elif minutes <= 9 * 60 + 00:  # 09:45 окончание 1 урока
        time_left = "До конца первого урока осталось " + str(9 * 60 + 00 - minutes) + " минут"
    elif minutes <= 9 * 60 + 55:  # 10:40 окончание 2 урока
        time_left = "До конца второго урока осталось " + str(9 * 60 + 55 - minutes) + " мин."
    elif minutes <= 10 * 60 + 45:  # 11:45 окончание 3 урока
        time_left = "До конца третьего урока осталось " + str(10 * 60 + 45 - minutes) + " мин."
    elif minutes <= 11 * 60 + 50:  # 12:50 окончание 4 урока
        time_left = "До конца четвертого урока осталось " + str(11 * 60 + 50 - minutes) + " мин."
    elif minutes <= 12 * 60 + 55:  # 13:55 окончание 5 урока
        time_left = "До конца пятого урока осталось " + str(12 * 60 + 55 - minutes) + " мин."
    elif minutes <= 13 * 60 + 55:  # 14:55 окончание 6 урока
        time_left = "До конца шестого урока осталось " + str(13 * 60 + 55 - minutes) + " мин."
    else:
        time_left = "Уроки на сегодня кончились"  # "Уроки на сегодня кончились"

    print(f"До конца урока осталось: {time_left}")

    return time_left


def shed_for_day(dic, shed) -> str:
    text = shed[shed.find("w" + str(dic["день_недели"])) + 3:]
    text = text[:text.find("w")]
    return text


def help() -> str:
    text = ("как использовать бот?\n Вводить команды можно не по порядку, при этом обязательно надо указывать класс"
            "ключ - что делает\n"
            "9А   - выдать расписание класса на сегодня\n"
            "10ХБ следующий   - выдать следующий урок 10х/б класса\n"
            "11ФМ понедельник - выдать расписание 11х/б класса на понедельник\n"
            "вт 9А - выдать расписание 9A класса на вторник (сокращения пн вт ср чт пт сб вс)\n"
            "9A.  - выдать расписание на сегодня и вывести время до конца урока\n")
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
