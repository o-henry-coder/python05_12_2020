import telebot
bot = telebot.TeleBot("1665630170:AAHjmfsyNdNp0Cmo8gWm5x1NK3SfNOf5H3E", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")



bot.polling()