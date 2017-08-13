# -*- coding: utf-8 -*-

import config
import telebot
import os
import random

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['pug'])
def find_file_ids(message):
	img_total = len(os.listdir('img/'))
	img_name = random.randint(1, img_total)

	f = open(config.img_dir +'{}.jpg'.format(img_name), 'rb')
	msg = bot.send_photo(message.chat.id, f, None)
	# bot.send_message(message.chat.id, msg.photo[-1].file_id, reply_to_message_id = msg.message_id)


@bot.message_handler(content_types=['text'])
def repeat(message):
	bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)