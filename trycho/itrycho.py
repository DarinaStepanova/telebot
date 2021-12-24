def pitsahi(message):
    bot.send_message(message.chat.id, 'лови')
    bot.send_photo(message.chat.id, photo=open('../kul/pictures/pitsa.png', 'rb'))
def pitsaoliv(message):
    bot.send_message(message.chat.id, 'осталась с маслинами') and bot.send_photo(message.chat.id, photo=open(
        '../kul/pictures/pitsasolivkami.png', 'rb'))
pitsa = pitsahi, pitsaoliv
