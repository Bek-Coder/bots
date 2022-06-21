import telebot


bot = telebot.TeleBot("5152368089:AAGQ0RIDsFKdcfkE5j5TwHnFW5e03pQ3w4U")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message,'Assalomu alaykum !')
    
@bot.message_handler()
def messageee(message):
    bot.send_message(message.chat.id,f"Bot azolari !")
print("Bot serverda ...")            
bot.polling(non_stop=True)