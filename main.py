#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Foxbot-3eb031550f0d.json', scope)
gs = gspread.authorize(credentials)
wks = gs.open('Bot').sheet1
print(wks.get_all_records())
print(wks.id)

bot = telebot.TeleBot("1057333385:AAHVpjye3rMi5T0oLunUnIeOmYP9kDe2KGU")
# bot.config['api_key'] = "1057333385:AAHVpjye3rMi5T0oLunUnIeOmYP9kDe2KGU"

# bot.send_message(410905220, "test")
# upd = bot.get_updates()
# print(upd)
# last_upd = upd
# message_from_user = last_upd.message
# print(message_from_user)
print(bot.get_me())

def log(message, answer):
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)

@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, "Вас приветствует команда FoxEducation \n" 
                                     "Мы поможем Вам прокачать ваши навыки в естественно-научном направлении. " 
                                     "А также подготовить к поступлению в специализированные школы и стать лучше. \n" 
                                     "Для получения полной информации оставьте, пожалуйста Ваши данные, и мы Вам обязательно перезвоним \n" 
                                     "Для регистрации нажмите /registration")
name = ' ';
number = 0;
subject = ' ';
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text=='/registration':
        bot.send_message(message.from_user.id, "Как можно к Вам обращаться?" )
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, "Для регистрации нажмите /registration")

def get_name(message): #получаем фамилию
    global name,wks
    name = message.text
    # wks = client.openall()
    bot.send_message(message.from_user.id, 'Введите ваш номер телефона: 87...');
    bot.register_next_step_handler(message, get_number);

def get_number(message):
    global number;
    number = message.text;
    bot.send_message(message.from_user.id, 'Какой предмет вы хотите изучать?');
    bot.register_next_step_handler(message, get_subject);

def get_subject(message):
    global subject
    subject = message.text
    bot.send_message(message.from_user.id, "Спасибо, Мы Вам перезвоним")
    wks.append_row([name, number, subject])

bot.polling(none_stop=True, interval=0)

upd = bot.get_updates()
print(upd)
