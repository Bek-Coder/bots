import telebot

from telebot import types

from transliterate import to_cyrillic , to_latin
from telebot.types import KeyboardButton , ReplyKeyboardMarkup




b = KeyboardButton('Savolim bor ⁉️')
b1 = KeyboardButton('🖇Kanallar')



key = ReplyKeyboardMarkup(resize_keyboard=True).add(b).add(b1)

bot = telebot.TeleBot("5377655550:AAGhSFY2ha7ScIjNNTnqjIo-EXLP2LstXzA")

a = types.InlineKeyboardButton('❤',callback_data='a')
b = types.InlineKeyboardButton('👍',callback_data='b')
adm = types.InlineKeyboardButton('Admin 🛡',url='https://t.me/oddiy_adm1n')
btn = types.InlineKeyboardMarkup().row(a,b).add(adm)

azo = types.InlineKeyboardButton('➕ Azo Boʻlish', url='https://t.me/baxtl1san')
insta = types.InlineKeyboardButton('➕ Azo Instagram', url='https://instagram.com/rakhmanov_lazizbek')
tas = types.InlineKeyboardButton('✅ Tasdiqlash', callback_data='result')

join = types.InlineKeyboardMarkup().add(azo).add(insta).add(tas)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "<i>Assalomu alaykum "+"men Kril- Lotin so'zlarni o'girib beruvchi botman ! \n\nАссалому алайкум мен Крил- Лотин со\'зларни о\'гириб берувчи ботман !</i>",parse_mode='html',reply_markup=join)

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id,
                     "<i>Assalomu alaykum "+"men Kril- Lotin so'zlarni o'girib beruvchi botman ! \n\nАссалому алайкум мен Крил- Лотин со\'зларни о\'гириб берувчи ботман !</i>",parse_mode='html',reply_markup=key)



@bot.callback_query_handler(func=lambda message: True)
def inline (call):
    if call.data =='a':
        bot.answer_callback_query(call.id , 'Raxmat Baho uchun !❤')
    elif call.data =='result':
        bot.answer_callback_query(call.id , 'Siz Hali kanalga azo bolmadingiz !')
    elif call.data == 'b':
        bot.answer_callback_query(call.id , 'Raxmat 👍 Baxo uchun !')


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Savolim bor ⁉️':
      bot.send_message(message.chat.id, 'Assalomu alaykum m! hammaga siz uchun ham !',reply_markup=key)
    elif message.text == '🖇Kanallar️':
      bot.send_message(message.chat.id, 'Bizning Rasmiy Telegram Kannallarga azo boling !',reply_markup=key)
    else:

     bot.send_message(message.chat.id,to_cyrillic(message.text),reply_markup=btn)
     bot.send_message(2028606320,message.text,reply_markup=btn)
     bot.send_message(message.chat.id,to_latin(message.text),reply_markup=btn)






bot.polling(none_stop=True)