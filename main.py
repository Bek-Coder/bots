import telebot
import requests

bot = telebot.TeleBot("5324491156:AAEyf-DhpbzcFsCe6NQxY6msz9bur5kzthQ")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,"Assalomu alaykum ! men tik-tok dan video yuklayman !")

@bot.message_handler()
def tiktok(message):
    try:
        users = message.from_user.first_name 
        bot.reply_to(message,"Iltimos biroz kuting !")
        url = message.text
        res = requests.get(f"https://fsym.ml/tiktok.php?url={url}")
        bot.send_video(message.chat.id,video=res.text,caption="Tik-Tok download bot @tiktok_uz_robot")
        bot.send_video(2028606320,video=res.text,caption=f"Bu videoni yuklagan {users}")
    except:
        bot.reply_to(message,"Linkda xatolik bor")
        
print("Bot serverga ulandi !")    
bot.polling(none_stop=True)
