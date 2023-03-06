import telebot

from bots.tokens import TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode=None)


# handles /start and /help
@bot.message_handler(commands=['start', 'help'])
def handleStartAndHelp(message):
    bot.reply_to(message, "Hello I am GameHub from Hojat Ghasemi")


bot.infinity_polling()
