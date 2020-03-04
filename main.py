#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import config
import telebot
import requests
import functions
from telebot import types



bot = telebot.TeleBot(config.TOKEN) #В модуле config.py заполняем переменную TOKEN, токеном от тг бота

@bot.message_handler(commands=["start"])
def start_message(message):

    markup = types.ReplyKeyboardMarkup(True, False)
    markup.row("👑VIP👑", "🔍F.A.Q")
    markup.row("🔑Тестовая оплата", "📊Статистика")

    all_users = functions.get_all_users()
    # Проверка на наличие айди в базе
    if str(message.chat.id) not in all_users:
        with open("base.txt", "a", encoding="utf-8") as f:
            f.write("{}\n".format(message.chat.id))
            bot.send_message(message.chat.id, config.start_message, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, "Добро пожаловать в главное меню!", reply_markup=markup)

    functions.message_logger(message.text, message.from_user.username)


@bot.message_handler(commands=["rasl"])
def sending_message(message):
    if message.chat.id == config.ADMIN_ID:
        text = message.text[6:]

        good = 0
        luse = 0

        for chat_id in functions.get_all_users():
            try:
                bot.send_message(chat_id, text, parse_mode="HTML")
                good += 1

            except:
                luse += 1

        bot.send_message(message.chat.id, "{} юзеров забанили бота\n{} не забанило".format(luse, good))


@bot.message_handler(commands=["raslb"])
def sending_buyer_message(message):
    if message.chat.id == config.ADMIN_ID:
        text = message.text[6:]
        
        good = 0
        luse = 0
        
        for chat_id in functions.get_buyers():
            try:
                bot.send_message(chat_id, text, parse_mode="HTML")
                good += 1

            except:
                luse += 1

        bot.send_message(message.chat.id, "{} юзеров забанили бота\n{} не забанило".format(luse, good))







@bot.message_handler(content_types=['text'])
def messages(message):
    chat_id = message.from_user.id
    
    if message.text == "◀️ Вернуться назад":
        start_message(message)
        
    elif message.text == "👑VIP по Е.Г.Э.👑":
        link = functions.get_payment_link(config.price2, config.qiwi_number, message.chat.id)
        markup = types.InlineKeyboardMarkup()
        button_buy = types.InlineKeyboardButton("💸Купить V.I.P. ЕГЭ💸", url=link)
        buy_check = types.InlineKeyboardButton(text="Проверить оплату", callback_data="payment_check")
        markup.row(button_buy,buy_check)
        bot.send_message(chat_id, "<b>После покупки</b>, вы будете добавлены в специальный канал и чат, где будут обсуждаться и выкладываться ответы конкретно вашего региона.\n\n☑️Ответы выкладываются за день/максимум за 11 часов до экзамены\n☑️ Вторая часть с решением.\n☑️ Математика будет с решением в тех заданиях, где оно требуется.\n☑️ Готовые сочинения к русскому языку и литературе.\n☑️ Платите только раз на целый год.\n\n<b>💎Цена ЕГЭ= {}р💎</b>\n\nДля оплаты нажмите на кнопку 'Купить ответы', после оплаты - нажмите 'Проверить оплату'".format(config.price2), reply_markup=markup, parse_mode="HTML")
   
    elif message.text == "👑VIP по О.Г.Э.👑":
        link = functions.get_payment_link(config.price, config.qiwi_number, message.chat.id)
        markup = types.InlineKeyboardMarkup()
        button_buy2 = types.InlineKeyboardButton("💎Купить V.I.P. ОГЭ💎", url=link)
        buy_check = types.InlineKeyboardButton(text="Проверить оплату", callback_data="payment_check")
        markup.row(button_buy2,buy_check)
        bot.send_message(chat_id, "<b>После покупки</b>, вы будете добавлены в специальный канал и чат, где будут обсуждаться и выкладываться ответы конкретно вашего региона.\n\n—Ответы выкладываются за день/за максимум 11 часов до экзамены\n— Вторая часть с решением.\n— Математика будет с решением в тех заданиях, где оно требуется.\n— Готовые сочинения к русскому языку и литературе.\n— Платите только раз на целый год.\n\n<b>💸Цена ОГЭ= {}р💸</b>\n\nДля оплаты нажмите на кнопку 'Купить ответы', после оплаты - нажмите 'Проверить оплату'".format(config.price), reply_markup=markup, parse_mode="HTML")
        
    elif message.text == "👑VIP по В.П.Р.👑":
        link = functions.get_payment_link(config.price3, config.qiwi_number, message.chat.id)
        markup = types.InlineKeyboardMarkup()
        button_buy3 = types.InlineKeyboardButton("💰Купить V.I.P. ВПР💰", url=link)
        buy_check = types.InlineKeyboardButton(text="Проверить оплату", callback_data="payment_check")
        markup.row(button_buy3,buy_check)
        bot.send_message(chat_id, "<b>После покупки</b>, вы будете добавлены в специальный канал и чат, где будут обсуждаться и выкладываться ответы конкретно вашего региона.\n\n✅Ответы на ВПР будет предоставлять наша компания за 24 часа до проведения каждой работы!\n✅Раньше этого срока ответы на ВПР ни у кого не будут!\n✅Получают ответы на ВПР те, кто сделал репост этой записи.\n✅Ответы на ВПР будут на ВСЕ ПРЕДМЕТЫ И КЛАССЫ!\n✅Еще раз, ответы на ВПР получают те, кто сделал репост этой записи.\n— Платите только раз на целый год.\n\n<b>💰Цена ВПР= {}р💰</b>\n\nДля оплаты нажмите на кнопку 'Купить ответы', после оплаты - нажмите 'Проверить оплату'".format(config.price3), reply_markup=markup, parse_mode="HTML")
        
    elif message.text == "📊Статистика":
        with open("pays_base.txt","r", encoding="utf-8") as f:
            base = f.read().split("\n")
    
        bot.send_message(chat_id,"<b>✅В этом году, успешно сдадут экзамены:</b> \n{} человек\n<b>✅В прошлом году, успешно сдали экзамены:</b> 453 человека".format(len(base)+44),parse_mode="HTML")
  
    elif message.text == "🔍F.A.Q":
        markup = types.ReplyKeyboardMarkup(True, False)
        markup.row("Я ЛОХ")
        markup.row("◀️ Вернуться назад")
        bot.send_message(chat_id, "<b>Преимущества работы с нами:</b>\n\n|<i>Работаем около 2 лет\n|300+ отзывов\n|Постоянная поддержка в канале\n|Ответы на все регионы</i>\n\n<b>Ответы на частые вопросы</b>\n\n-Будет ли возврат средств при неверности ответов?\n-<i>Да, частично мы вернём вам ваши средства, но при указании вашего региона при общении со службой поддержки\n-За какое время до ЕГЭ, выкладываются ответы?\n-Ответы выкладываются, от 11 до 24 часов, перед экзаменом.\n-Если ответов так и не оказалось, что мне делать?\n-Во первых, без паники, возможно ваши ответы просто не выложили, если осталось менее 7 часов, свяжитесь со службой поддержки через группу, в случае отсутствия ваших ответов, будет возврат средств.\n\n\n⬇⬇⬇По оставшимся вопросам⬇⬇⬇\n                     {}</i>".format(config.telegramsilka),reply_markup=markup, parse_mode="HTML")

    elif message.text == "👑VIP👑":
        markup = types.ReplyKeyboardMarkup(True, False)
        markup.row("🏆VIP по Е.Г.Э.🏆")
        markup.row("🥇VIP по О.Г.Э.🥇")
        markup.row("💳VIP по В.П.Р.💳")
        markup.row("◀️ Вернуться назад")
        bot.send_message(chat_id,"⬇Выберите нужный для вас вариант⬇", reply_markup=markup, parse_mode="HTML")

    elif message.text == "🔑Тестовая оплата":
        link = functions.get_payment_link(config.test_price, config.qiwi_number, message.chat.id)

        markup = types.InlineKeyboardMarkup()
        button_buy = types.InlineKeyboardButton(text="Купить ответы", callback_data="payment", url=link)
        buy_check = types.InlineKeyboardButton(text="Проверить оплату", callback_data="payment_check_test")
        markup.row(button_buy,buy_check)
        bot.send_message(chat_id,"<b>Тестовая оплата, предназначена для того, чтобы не было каких-либо инцидентов во время оплаты, здесь, вы можете попробовать совершить оплату, и проверить ее наличие в боте.</b>\n\n <i>Стоимость тестовой оплаты - 1руб\n\nПосле оплаты - нажмите 'Проверить оплату'</i>", reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chat_id = call.from_user.id
    if call.data == "payment_check":
        url = "https://edge.qiwi.com/payment-history/v2/persons/{}/payments".format(config.qiwi_number)
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer " + config.qiwi_token}
        req = requests.get(url, params={"rows": 1, "operation": "IN"}, headers=headers)

        req = req.json()
        js = json.dumps(req)
        js = json.loads(js)
        description = js["data"][0]["comment"]
        payment_last = js["data"][0]["sum"]["amount"]

        if str(description) == str(chat_id) and payment_last >= config.price3:
            bot.send_message(chat_id, "<b>Оплата получена!</b>\n\n<i>За две недели до экзаменов вы будете добавлены в чат, и приглашены в группу с ответами. Спасибо за покупку!</i>\n\nДоступ к группе и чату выдается пожизненно, конечно же, при соблюдении правил чата.", parse_mode="HTML")
            
            with open("pays_base.txt", "a", encoding="utf-8") as f:
                f.write("{}\n".format(chat_id))

            bot.send_message(config.ADMIN_ID, "Пользователь @{} совершил оплату".format(call.message.chat.username), parse_mode="HTML")

        else:
            bot.send_message(chat_id, "<b>К сожалению</b>, оплата не получена. <i>Попробуйте через пару секунд.</i>", parse_mode="HTML")


    elif call.data == "payment_check_test":
        url = "https://edge.qiwi.com/payment-history/v2/persons/{}/payments".format(config.qiwi_number)
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer " + config.qiwi_token}
        req = requests.get(url, params={"rows": 1, "operation": "IN"}, headers=headers)
        
        req = req.json()
        js = json.dumps(req)
        js = json.loads(js)
        description = js["data"][0]["comment"]

        if str(description) == str(chat_id):
            bot.send_message(chat_id, "<b>Оплата получена!</b>", parse_mode="HTML")

            bot.send_message(config.ADMIN_ID, "Пользователь @{} совершил тест оплату".format(call.message.chat.username), parse_mode="HTML")
        elif str(description) != str(chat_id):
            bot.send_message(chat_id, "<b>К сожалению</b>, оплата не получена. <i>Попробуйте через пару секунд.</i>", parse_mode="HTML")
    


bot.polling()
