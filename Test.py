import telebot
import config, wellcome, nature
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

text = ''
count = 0

@bot.message_handler(commands=['start'])

def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    types1 = types.InlineKeyboardButton('Продолжить', callback_data='go')
    markup.add(types1)
    photo = open('photo_welcome.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, wellcome.welcome_text, reply_markup=markup)
    bot.register_next_step_handler(message, text_user)





def text_user(message):
    global data_user
    global text
    try:
        text = str(message.text)
    except ValueError:
        bot.register_next_step_handler(message, text_user)
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Продолжить', callback_data='gogo')
    markup.add(item1)
    if text == '1' or text == '01':
        bot.send_message(message.chat.id, nature.nature_1, reply_markup=markup)
    elif text == '2' or text == '02':
        bot.send_message(message.chat.id, nature.nature_2, reply_markup=markup)
    elif text == '3' or text == '03':
        bot.send_message(message.chat.id, nature.nature_3, reply_markup=markup)
    elif text == '4' or text == '04':
        bot.send_message(message.chat.id, nature.nature_4, reply_markup=markup)
    elif text == '5' or text == '05':
        bot.send_message(message.chat.id, nature.nature_5, reply_markup=markup)
    elif text == '6' or text == '06':
        bot.send_message(message.chat.id, nature.nature_6, reply_markup=markup)
    elif text == '7' or text == '07':
        bot.send_message(message.chat.id, nature.nature_7, reply_markup=markup)
    elif text == '8' or text == '08':
        bot.send_message(message.chat.id, nature.nature_8, reply_markup=markup)
    elif text == '9' or text == '09':
        bot.send_message(message.chat.id, nature.nature_9, reply_markup=markup)
    else:
        text.split()
        if len(text[0]) < 3:
            number1 = int(text[0])
            number2 = int(text[1])
            count = number1 + number2
            if count > 9:
                count_list = list(str(count))
                number1 = int(count_list[0])
                number2 = int((count_list[1]))
                count = number1 + number2
                bot.send_message(message.chat.id, 'твое число: ' + str(count))
                if count == 1:
                    bot.send_message(message.chat.id, nature.nature_1, reply_markup=markup)
                    # bot.send_message(message.chat.id, wellcome.pay)
                    # bot.register_next_step_handler(message, wellcome.pay)
                elif count == 2:
                    bot.send_message(message.chat.id, nature.nature_2, reply_markup=markup)
                    # bot.register_next_step_handler(message)
                elif count == 3:
                    bot.send_message(message.chat.id, nature.nature_3, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 4:
                    bot.send_message(message.chat.id, nature.nature_4, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 5:
                    bot.send_message(message.chat.id, nature.nature_5, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 6:
                    bot.send_message(message.chat.id, nature.nature_6, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 7:
                    bot.send_message(message.chat.id, nature.nature_7, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 8:
                    bot.send_message(message.chat.id, nature.nature_8, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 9:
                    bot.send_message(message.chat.id, nature.nature_9, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
            else:
                bot.send_message(message.chat.id, 'твое число: ' + str(count))
                if count == 1:
                    bot.send_message(message.chat.id, nature.nature_1, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 2:
                    bot.send_message(message.chat.id, nature.nature_2, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 3:
                    bot.send_message(message.chat.id, nature.nature_3, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 4:
                    bot.send_message(message.chat.id, nature.nature_4, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 5:
                    bot.send_message(message.chat.id, nature.nature_5, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 6:
                    bot.send_message(message.chat.id, nature.nature_6, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 7:
                    bot.send_message(message.chat.id, nature.nature_7, reply_markup=markup)
                    # bot.register_next_step_handler(message, )
                elif count == 8:
                    bot.send_message(message.chat.id, nature.nature_8, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)
                elif count == 9:
                    bot.send_message(message.chat.id, nature.nature_9, reply_markup=markup)
                    # bot.register_next_step_handler(message, payment)




@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'go':
            bot.send_message(call.message.chat.id, wellcome.welcome_next)
            bot.send_message(call.message.chat.id, wellcome.rasklad)
        elif call.data == 'gogo':
            bot.send_message(call.message.chat.id, wellcome.second)
            bot.send_message(call.message.chat.id, wellcome.pay)


bot.polling(none_stop=True)