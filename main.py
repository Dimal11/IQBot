import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


@bot.message_handler(commands=['start'])
def start_menu(m, res=False):
    user_name = m.from_user.first_name
    buttons = ('Button 1', 'Button 2', 'Button 3')
    for btn in buttons:
        markup.add(types.KeyboardButton(str(btn)))
    bot.send_message(m.chat.id, f'Привет {user_name}!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def sub_menu(message):
    if message.text == 'Button 1':
        buttons = ('Sub_Button1', 'Sub_Button 2', 'Back')
        for btn in buttons:
            markup.add(types.KeyboardButton(str(btn)))
    elif message.text == 'Back':
        pass


# bot.forward_message(os.getenv('TO_CHAT_ID'), message.chat.id, message.message_id)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
