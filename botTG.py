import telebot
from bs4 import BeautifulSoup
import requests
bot = telebot.TeleBot('urToken')

help_string = []
help_string.append("Справка об командах:\n\n")
help_string.append("/menu - меню с функциями;\n")
help_string.append("/ineedhelp - обратиться за помощью;\n")


@bot.message_handler(commands=['help'])
def send_help(message):
    # отправка сообщения с поддержкой разметки Markdown
    bot.send_message(message.chat.id, "".join(help_string), parse_mode="Markdown")


@bot.message_handler(commands=['ineedhelp'])
def send_helper(message):
    bot.send_message(message.chat.id, 'Обратиться за помощью к нему')


@bot.message_handler(commands=['menu'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Парсинг', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Профиль', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Ссылки', callback_data=3))
    bot.send_message(message.chat.id, text="Вот мои функции выбирай:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)  # <=== Если мы отправили ответ,
    # то после ответа, клавиатура будет исчезать из чата
    bot.answer_callback_query(callback_query_id=call.id, text='Ok')
    if call.data == '1':
        answer = 'Ты выбрал 1 кнопку'
    elif call.data == '2':
        answer = 'Ты выбрал 2 кнопку'
   elif call.data == '3':
        answer = 'Ты выбрал 3 кнопку'

    bot.send_message(call.message.chat.id, answer)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, напиши /help')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Пока :)')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
