import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Найти авто", "Оценить машину")
    markup.add("Выгодное объявление", "Просто спросить")
    bot.send_message(message.chat.id, f"Здарова, Михайло 👊 Чем займёмся?", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Найти авто":
        bot.send_message(message.chat.id, "Введи параметры, по которым ищем авто (марка, модель, бюджет и т.д.)")
    elif message.text == "Оценить машину":
        bot.send_message(message.chat.id, "Скинь ссылку на объявление — я приценю по нашей базе 🧠")
    elif message.text == "Выгодное объявление":
        bot.send_message(message.chat.id, "Секунду, Михайло… Сейчас найду самое выгодное предложение 🔎")
    elif message.text == "Просто спросить":
        bot.send_message(message.chat.id, "Спрашивай что угодно — я всегда на связи! 🧠")
    else:
        bot.send_message(message.chat.id, "Не понял, брат 😅 Нажми на кнопку или уточни")

bot.polling()