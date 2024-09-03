import telebot

TOKEN = 'BOT_TOKEN'

WEBHOOK_URL = 'WEB_SITE'

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)
