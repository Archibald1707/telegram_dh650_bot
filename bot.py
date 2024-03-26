import telebot
from secrets import secrets
from telebot import types
from projects import projects

token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("Старт")
    projects_button = types.KeyboardButton("Проекты")
    markup.add(start_button, projects_button)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}\nЧто по плану на сегодня?".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def buttons(message):
    if (message.text == "Старт"):
        bot.send_message(message.chat.id, text="Давай уже выбирай что мне делать >:(")
    elif (message.text == "Проекты"):
        for project in projects:
            bot.send_message(message.chat.id, text=f"{project}")
    else:
        bot.send_message(message.chat.id, text="Я могу отвечать только на нажатие кнопок.")

# бесконечное выполнение кода
bot.polling(none_stop=True, interval=0)