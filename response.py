from current_lesson import *

def m_response(dic) -> str:
    dic["день_недели"] = 0

    # читаем все расписание
    shed = read_schedule_file()
    # оставляем только расписание указанного класса
    shed = shed[shed.find(dic["класс"]) + 1:]
    shed = shed[shed.find("\n") + 1:]
    answer = "---"
    if dic["следующий"] == 1:
        answer = next_lesson(dic, shed)  # следующий урок
    elif dic["осталось"] == 1:
        answer = remaind(dic, shed)  # осталось до конца урока
    elif dic["вся неделя"] == 1:
        answer = "-" #all_week(dic, shed)
    else:
        answer = shed_for_day(dic, shed)

    return answer


def next_lesson(dic, shed) -> str:
    lesson = cur_lesson() + 1
    text = shed[shed.find("w" + str(dic["день_недели"])) + 3:]
    text = text[text.find(str(lesson)) + 2:]
    text = text[:text.find("\n")]

    return text


def remaind(dic, shed):


    return text


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
