import telebot

TOKEN = '7275258384:AAHTX92bfd4l27dHI322pl9pJZh8BGso6bg'

WEBHOOK_URL = 'https://d4ca-95-214-210-98.ngrok-free.app'

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)
