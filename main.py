# -*- coding: utf-8 -*-

import requests  
import datetime
from bot import *

token = '423706561:AAEq3oNCBAZ02ogfTnaKpf66W9yPhw4fAts'

greet_bot = BotHandler(token)
now = datetime.datetime.now()
 
def main():  
    new_offset = None
    today = now.day
    hour = now.hour
 
    while True:
        greet_bot.get_updates(new_offset)
 
        last_update = greet_bot.get_last_update()
 
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
 
        if today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, u'Доброе утро, {}'.format(last_chat_name))
            today += 1
 
        elif today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, u'Добрый день, {}'.format(last_chat_name))
            today += 1
 
        elif today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, u'Добрый вечер, {}'.format(last_chat_name))
            today += 1
 
        new_offset = last_update_id + 1
 
if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()