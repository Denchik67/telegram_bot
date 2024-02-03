import telebot
import config
import datetime
import sys

def main():
    bot = telebot.TeleBot(config.TOKEN)
    print("бот успешно стартовал")
    @bot.message_handler(content_types=['text'])
    def lalala(message):
        text =""
        if int(message.text) == 9:
            text = ("9A \n "
                    "понедельник\n"
                    "0 -----\n"
                    "1 Английский\n"
                    "2 Алгебра\n"
                    "3 Физика\n"
                    "4 Русский\n"
                    "5 История\n"
                    "6 Литература\n"
                    "--------------\n"
                    "0 -----\n"
                    "1 Английский\n"
                    "2 Алгебра\n"
                    "3 Физика\n"
                    "4 Русский\n"
                    "5 История\n"
                    "6 Литература\n")


        now = datetime.datetime.today()
        minutes = int(now.strftime("%H"))*60 + int(now.strftime("%M"))

        if minutes < 8*60 + 20:
            current_lesson = "Уроки не начались"
        elif minutes <= 9*60 + 00:
            current_lesson = 0
        elif minutes <= 9*60 + 55:
            current_lesson = 1
        elif minutes <= 10*60 + 45:
            current_lesson = 2
        elif minutes <= 11*60 + 50:
            current_lesson = 3
        elif minutes <= 12*60 + 55:
            current_lesson = 4
        elif minutes <= 13*60 + 55:
            current_lesson = 5
        elif minutes <= 14*60 + 55:
            current_lesson = 6
        elif minutes <= 15*60 + 45:
            current_lesson = 7
        else:
            current_lesson = 8 #"Уроки на сегодня кончились"


        #bot.send_message(message.chat.id, text)
        #now = datetime.datetime.today()
        #bot.send_message(message.chat.id, str(now.weekday()))
        #current_time = now.strftime("%H:%M:%S")
        # bot.send_message(message.chat.id, current_time)
        bot.send_message(message.chat.id, "сейчас " + str(current_lesson) + " урок, следующий " + str(current_lesson + 1) + " урок")
        print("log:>" + message.text)
        print("log:<" + "сейчас " + str(current_lesson) + " урок, следующий " + str(current_lesson + 1) + " урок")
    # RUN
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()