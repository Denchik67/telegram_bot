from current_lesson import *

# Значения по умолчанию, dic (dictionary) - словарь
dic = {
    "день_недели": current_day(),  # Нужно вводить текущий день недели
    "урок": cur_lesson(),  # Текущий урок
    "вся_неделя": 0,  # Вывести уроки на всю неделю
    "класс": "",
    "ошибка": 1,
    "следующий": 0,
    "осталось": 0
}


def parser(str_to_parse) -> {}:
    parser_week_days(str_to_parse, dic)
    parser_class(str_to_parse, dic)
    parser_whole_week(str_to_parse, dic)
    parser_remain_to_end_of_lesson(str_to_parse, dic)
    parser_next(str_to_parse, dic)
    return dic


def parser_week_days(str_to_parse, dic):
    s = str_to_parse.lower()
    # определение дня недели
    if s.find(" пн") >= 0 or s.find("понедельник") >= 0:
        dic["день_недели"] = 0
        dic["ошибка"] = 0
    elif s.find(" вт") >= 0 or s.find("вторник") >= 0:
        dic["день_недели"] = 1
        dic["ошибка"] = 0
    elif s.find(" ср") >= 0 or s.find("среда") >= 0:
        dic["день_недели"] = 2
        dic["ошибка"] = 0
    elif s.find(" чт") >= 0 or s.find("четверг") >= 0:
        dic["день_недели"] = 3
        dic["ошибка"] = 0
    elif s.find(" пт") >= 0 or s.find("пятница") >= 0:
        dic["день_недели"] = 4
        dic["ошибка"] = 0
    elif s.find(" сб") >= 0 or s.find("суббота") >= 0:
        dic["день_недели"] = 5
        dic["ошибка"] = 0
    elif s.find(" вс") >= 0 or s.find("воскресенье") >= 0:
        dic["день_недели"] = 6
        dic["ошибка"] = 0
    elif s.find("завтра") >= 0:
        if current_day() == 6:
            dic["день_недели"] = 0
            dic["ошибка"] = 0
        else:
            dic["день_недели"] = current_day() + 1
            dic["ошибка"] = 0


#  parser_class определение класса
def parser_class(str_to_parse, dic):
    s = str_to_parse.upper()
    if s.find("5А") >= 0 or s.find("5A") >= 0:
        dic["класс"] = "5А"
        dic["ошибка"] = 0
    elif s.find("5Б") >= 0:
        dic["класс"] = "5Б"
        dic["ошибка"] = 0
    elif s.find("5В") >= 0 or s.find("5B") >= 0:
        dic["класс"] = "5B"
        dic["ошибка"] = 0
    elif s.find("6А") >= 0 or s.find("6A") >= 0:
        dic["класс"] = "6А"
        dic["ошибка"] = 0
    elif s.find == "6Б":
        dic["класс"] = "6Б"
        dic["ошибка"] = 0
    elif s.find("6В") >= 0 or s.find("6B") >= 0:
        dic["класс"] = "6B"
        dic["ошибка"] = 0
    elif s.find("7А") >= 0 or s.find("7А") >= 0:
        dic["класс"] = "7А"
        dic["ошибка"] = 0
    elif s.find == "7Б":
        dic["класс"] = "7Б"
        dic["ошибка"] = 0
    elif s.find("8А") >= 0 or s.find("8A") >= 0:
        dic["класс"] = "8А"
        dic["ошибка"] = 0
    elif s.find == "8Б":
        dic["класс"] = "8Б"
        dic["ошибка"] = 0
    elif s.find("8В") >= 0 or s.find("8B") >= 0:
        dic["класс"] = "8B"
        dic["ошибка"] = 0
    elif s.find("9А") >= 0 or s.find("9A") >= 0:
        dic["класс"] = "9А"
        dic["ошибка"] = 0
    elif s.find == "9Б":
        dic["класс"] = "9Б"
        dic["ошибка"] = 0
    elif s.find("10А") >= 0 or s.find("10A") >= 0:
        dic["класс"] = "10А"
        dic["ошибка"] = 0
    elif s.find("11А") >= 0 or s.find("11A") >= 0:
        dic["класс"] = "11А"
        dic["ошибка"] = 0


def parser_whole_week(str_to_parse, dic):
    s = str_to_parse.lower()
    if s.find("неделя") >= 0:
        dic["вся_неделя"] = 1


def parser_remain_to_end_of_lesson(s, dic):
    if s.find(".") >= 0:
        dic["осталось"] = 1


def parser_next(s, dic):
    if s.find("след") >= 0 or s.find("следующий") >= 0:
        dic["следующий"] = 1

