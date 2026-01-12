import logging
import telebot
import requests
import urllib.parse

bot = telebot.TeleBot("8288949230:AAGpjRx054z6ZvNCu0ygMQujTD4aJrg_t7s")

u = lambda p: "https://image.pollinations.ai/prompt/" + urllib.parse.quote_plus(p)

@bot.message_handler(func=lambda m: True)
def g(m):
    b = requests.get(u(m.text)).content
    bot.send_photo(m.chat.id, b, caption=m.text)

bot.infinity_polling()
