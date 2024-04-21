# telebot - это библиотека для работы с телеграм
import telebot
# config - это библиотека, предназначенная для управления конфигурационными файлами
import config
# функции из файла current_lesson.py "import *" - означает все функции из файла
from current_lesson import *
from response import *
from myparser import *

# main - главная функция откуда стартует программа
def main():
    bot = telebot.TeleBot(config.TOKEN)
    print("бот успешно стартовал по адресу https://t.me/lessons_of_273bot")

    @bot.message_handler(content_types=['text'])
    def lalala(message):
        # парсинг того что нам написали в бот (команды)
        answer = ""
        dic = parser(message.text)
        if dic["ошибка"] == 1:
            res = " 😔 ошибка\n" + help()
            bot.send_message(message.chat.id, res)
        else:
            # подготовка ответа на запрос
            answer = m_response(dic)
            # отправка ответа
            bot.send_message(message.chat.id, answer)

        # запись лога в консоль
        print(current_time() + ": log:> " + message.text + "\n" +
              answer + "\n" +
              "--------------------------------------------\n")

    # RUN
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
