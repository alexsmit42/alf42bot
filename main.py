# -*- coding: utf-8 -*-

import config
import telebot
import random
import re
from pathlib import Path

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['menu'])
def show_menu(message):
	markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	markup.row('/pug', '/random_pug')
	bot.send_message(message.chat.id, "Choose command:", reply_markup=markup)

@bot.message_handler(commands=['random_pug'])
def random_photo(message):
	img_name = random.randint(1, config.img_total)

	f = open(config.img_dir +'{}.jpg'.format(img_name), 'rb')
	msg = bot.send_photo(message.chat.id, f, None)
	# bot.send_message(message.chat.id, msg.photo[-1].file_id, reply_to_message_id = msg.message_id)

@bot.message_handler(commands=['pug'])
def generate_keyboard(message):
	markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

	for i in range(1, config.img_total)[::3]:
		if i+2 > config.img_total:
			markup.row(str(i), str(i+1))
		else:
			markup.row(str(i), str(i+1), str(i+2))

	bot.send_message(message.chat.id, "Choose pug: ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def find_pug(message):
	text = re.sub(r'[^0-9]', '', message.text)
	filename = config.img_dir +'{}.jpg'.format(text)

	if Path(filename).is_file():
		f = open(filename, 'rb')
		bot.send_photo(message.chat.id, f, None)
	else:
		bot.send_message(message.chat.id, 'Hello, {}!'.format(message.chat.first_name))

if __name__ == '__main__':
    bot.polling(none_stop=True)