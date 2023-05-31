# подключение библиотек, реализация хостинга Google Colab
# В Google colab добавить отдельным первым кодом: !pip install pyTelegramBotAPI
# для установки необходимо в файл requirements.text добавить строку
# 'PyTelegramBotApi'

from telebot import TeleBot, types
import random


bot = TeleBot(token='I_NEED_YOU_REAL_TOKEN!!!', parse_mode='html') # создание бота

#библиотека с функциями SQL:
baza = ["Оператор SQL SELECT -\nhttp://2sql.ru/basic/sql-select/", "Оператор SQL INSERT -\nhttp://2sql.ru/basic/sql-insert/", "Оператор SQL UPDATE -\nhttp://2sql.ru/basic/sql-update/","Оператор SQL WHERE -\nhttp://2sql.ru/basic/sql-where/", "Оператор SQL ORDER BY -\nhttp://2sql.ru/basic/sql-order-by/", "Оператор SQL GROUP BY -\nhttp://2sql.ru/basic/sql-group-by/", "Оператор SQL HAVING -\nhttp://2sql.ru/basic/sql-having/", "Оператор SQL DISTINCT -\nhttp://2sql.ru/basic/sql-distinct/", "Операторы SQL AND и OR -\nhttp://2sql.ru/basic/sql-and-or/"]
join = ["Оператор SQL INNER JOIN -\nhttp://2sql.ru/advanced/sql-inner-join/", "Оператор SQL LEFT JOIN -\nhttp://2sql.ru/advanced/sql-left-join/", "Оператор SQL RIGHT JOIN -\nhttp://2sql.ru/advanced/sql-right-join/", "Оператор SQL FULL JOIN -\nhttp://2sql.ru/novosti/sql-full-join/", "Оператор SQL CROSS JOIN -\nhttp://2sql.ru/advanced/sql-cross-join/"]
agregat = ["Функция SQL COUNT() -\nhttp://2sql.ru/functions/sql-count/", "Функция SQL AVG() -\nhttp://2sql.ru/functions/sql-avg/", "Функция SQL MIN() -\nhttp://2sql.ru/functions/sql-min/", "Функция SQL MAX() -\nhttp://2sql.ru/functions/sql-max/", "Функция SQL SUM() -\nhttp://2sql.ru/functions/sql-sum/", "Функция SQL ROUND() -\nhttp://2sql.ru/functions/sql-round/", "Функция SQL FIRST() -\nhttp://2sql.ru/functions/sql-first/", "Функция SQL LAST() -\nhttp://2sql.ru/functions/sql-last/", "Функция SQL LEN() -\nhttp://2sql.ru/functions/sql-len/", "Функция SQL MID() -\nhttp://2sql.ru/functions/sql-mid/", "Функция SQL NOW() -\nhttp://2sql.ru/functions/sql-now/"]
dopom = ["SQL LIMIT -\nhttp://2sql.ru/advanced/sql-limit/", "SQL LIKE -\nhttp://2sql.ru/advanced/sql-like/", "Оператор SQL IN -\nhttp://2sql.ru/advanced/sql-in/", "Оператор SQL NOT -\nhttp://2sql.ru/advanced/sql-not/", "Оператор SQL AS -\nhttp://2sql.ru/advanced/sql-as/", "Оператор SQL BETWEEN -\nhttp://2sql.ru/advanced/sql-between/"]

# обработка команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Основы SQL")
    btn2 = types.KeyboardButton("JOIN")
    btn3 = types.KeyboardButton("Агрегатные функции")
    btn4 = types.KeyboardButton("Про эти функции полезно знать⚡️")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Давай вместе вспомним про SQL!!!\nСмелее, друг мой!!! Делай свой выбор, БД ждут нас😉".format(message.from_user), reply_markup=markup)
    bot.send_video(message.chat.id, 'https://media.giphy.com/media/LWJ7cKyiWPCnVyuAhT/giphy.gif', None, 'Text')

# обработка всех остальных сообщений    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Основы SQL"):
     bot.send_message(message.chat.id,"Отличный выбор, полезная информация 💯  :\n\n{0}".format(random.choice(baza)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("⭐️СПАСИБО♥️Я ВЕРНУСЬ⭐️")
     btn2 = types.KeyboardButton("Другой оператор")
     btn3 = types.KeyboardButton("Main Page✅")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Думаешь на сегодня достаточно?😎", reply_markup=markup)

    elif(message.text == "Другой оператор"):
      bot.send_message(message.chat.id,"Отличный выбор, полезная информация 💯  :\n\n{0}".format(random.choice(baza)))
      bot.send_message(message.chat.id,text="Продолжим? Точно знаю, что увлекает☺️")

    elif(message.text == "JOIN"):
     bot.send_message(message.chat.id,"Отличный выбор, полезная информация 💯  :\n\n{0}".format(random.choice(join)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("⭐️СПАСИБО♥️Я ВЕРНУСЬ⭐️")
     btn2 = types.KeyboardButton("Другой Join")
     btn3 = types.KeyboardButton("Main Page✅")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Думаешь на сегодня достаточно?😎", reply_markup=markup)

    elif message.text == "Другой Join":
      bot.send_message(message.chat.id,"Отличный выбор, полезная информация 💯  :\n\n{0}".format(random.choice(join)))
      bot.send_message(message.chat.id,text="Продолжим? Точно знаю, что увлекает☺️")

    elif(message.text == "Агрегатные функции"):
     bot.send_message(message.chat.id,"Отличный выбор, полезная информация 💯  :\n\n{0}".format(random.choice(agregat)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("⭐️СПАСИБО♥️Я ВЕРНУСЬ⭐️")
     btn2 = types.KeyboardButton("Другую функцию")
     btn3 = types.KeyboardButton("Main Page✅")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Думаешь на сегодня достаточно?😎", reply_markup=markup)

    elif message.text == "Другую функцию":
      bot.send_message(message.chat.id,"Отличный выбор, полезная информация 💯  :\n\n{0}".format(random.choice(agregat)))
      bot.send_message(message.chat.id,text="Продолжим? Точно знаю, что увлекает☺️")

    elif(message.text == "Про эти функции полезно знать⚡️"):
     bot.send_message(message.chat.id,"Отличный выбор, полезная информация 💯  :\n\n{0}".format(random.choice(dopom)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("⭐️СПАСИБО♥️Я ВЕРНУСЬ⭐️")
     btn2 = types.KeyboardButton("Другую полезность")
     btn3 = types.KeyboardButton("Main Page✅")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Думаешь на сегодня достаточно?😎", reply_markup=markup)

    elif message.text == "Другую полезность":
      bot.send_message(message.chat.id,"Отличный выбор, полезная информация 💯  :\n\n{0}".format(random.choice(dopom)))
      bot.send_message(message.chat.id,text="Продолжим? Точно знаю, что увлекает☺️")

    
    
    elif(message.text == "⭐️СПАСИБО♥️Я ВЕРНУСЬ⭐️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        markup.add(btn1)
        bot.send_message(message.chat.id,text="Всегда рад!🧡", reply_markup=markup)
        bot.send_video(message.chat.id, 'https://gifdb.com/images/file/thank-you-thank-you-498-x-280-gif-gmdo4mccdoejrzns.gif', None, 'Text')
    
    elif (message.text == "Main Page✅"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Основы SQL")
        btn2 = types.KeyboardButton("JOIN")
        btn3 = types.KeyboardButton("Агрегатные функции")
        btn4 = types.KeyboardButton("Про эти функции полезно знать⚡️")
     
        markup.add(btn1, btn2, btn3, btn4,)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню😉", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Не могу понять...😳Жмякни кнопку🙃")


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()

#Python✅ можно доработать под новый проект, помогашка)
