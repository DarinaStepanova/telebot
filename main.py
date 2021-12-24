import telebot
from telebot import types

token="2110095112:AAHFNzujkArHMLpZ60vUBiIDT7vaaZT1FJM"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add("Да, хочу", "Хочу питсу", "Расписание", "Когда очка?", "/help", "/settings", "/location", "/contacts", "/news")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею искать новости о МТУСИ\n\n'
                                      '/contacts - Контакты Университета\n'
                                      '/location - где находится МТУСИ\n'
                                      '/news - самые свежие новости\n'
                                      '/settings - настрой меня\n\n'
                                      'Нужно расписание? - Я помогу!\n'
                                      'Когда очка? - Скоро узнаем\n\n'
                                      'P.S. скажи, что хочешь питсу, - я умею бросаться ею')


@bot.message_handler(commands=['settings'])
def start_message(message):
    bot.send_message(message.chat.id, '--')


@bot.message_handler(commands=['news'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/about_the_university/news/')


@bot.message_handler(commands=['contacts'])
def start_message(message):
    bot.send_message(message.chat.id, '____________Контакты Университета____________\n'
                                      '\n'
                                      'МТУСИ на Авиамоторной\n'
                                      '111024, г. Москва, улица Авиамоторная, дом 8а\n'
                                      'Телефон\n'
                                      '+7 (495) 957-77-31\n'
                                      '+7 (495) 957-77-36\n'
                                      'Email\n'
                                      'mtuci@mtuci.ru\n')


@bot.message_handler(commands=['location'])
def start_message(message):
    locating = types.ReplyKeyboardMarkup()
    bot.send_location(message.chat.id, latitude=55.755296, longitude=37.712099, reply_markup=locating)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "да, хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "когда очка?":
        bot.send_message(message.chat.id, 'Следи за новостями на сайте МТУСИ')
    elif message.text.lower() == "хочу питсу":
        bot.send_message(message.chat.id, 'лови')
        bot.send_photo(message.chat.id, photo=open('kul/pictures/pitsa.png', 'rb'))
    elif message.text.lower() == "расписание":
        bot.send_message(message.chat.id, 'https://mtuci.ru/time-table/')
    elif message.text.lower():
        bot.send_message(message.chat.id, 'Пожалуйста, воспульзуйся одной из кнопок')


bot.polling()