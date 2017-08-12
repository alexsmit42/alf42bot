# -*- coding: utf-8 -*-

import requests  
import datetime
from bot import *

token = '423706561:AAEq3oNCBAZ02ogfTnaKpf66W9yPhw4fAts'

greet_bot = BotHandler(token)
now = datetime.datetime.now()
 
def main():  
    print 666666
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
 
        greet_bot.send_message(last_chat_id, u'Доброе утро, {} (В ответ на: {})'.format(last_chat_name, last_chat_text))
 
        new_offset = last_update_id + 1
 
if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()