import telebot
import requests
import sqlite3

db = sqlite3.connect("baza.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS chatid(id INT)""")
db.commit()

bot = telebot.TeleBot("5324491156:AAEyf-DhpbzcFsCe6NQxY6msz9bur5kzthQ")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,"<b>Assalomu alaykum ! men 🎵 Tik-Tok &🔥 Instagram va🟥 Youtube dan video yuklayman!\n\n Link yuboring !</b>",parse_mode='html')
    try:
        sql.execute("INSERT INTO chatid VALUES(?)",(message.chat.id))
        db.commit()
    except:
        pass

@bot.message_handler()
def tiktok(message):
           
    try:
        if message.text == '/stat': 
            try:
                data = sql.execute("SELECT COUNT(id) FROM chatid")
                bot.send_message(message.chat.id,f"Bot azosi !{data}")
            except:
                pass
        else:
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
