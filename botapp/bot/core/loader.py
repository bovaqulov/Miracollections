from telebot import TeleBot
from telebot.types import BotCommand 


from mirasite.settings import BOT_TOKEN


bot = TeleBot(token=BOT_TOKEN, threaded = False, use_class_middlewares=True, parse_mode="html")

bot.set_my_commands(commands=([
		BotCommand("start", "Restart 🚀")
	]))

def middle():
    from telebot.handler_backends import BaseMiddleware
    from telebot.handler_backends import CancelUpdate

    class SimpleMiddleware(BaseMiddleware):
        def __init__(self, limit) -> None:
            super().__init__()
            self.last_time = {}
            self.limit = limit
            self.update_types = ['message']

        def pre_process(self, message, data):
            if not message.from_user.id in self.last_time:
                self.last_time[message.from_user.id] = message.date
                return
            if message.date - self.last_time[message.from_user.id] < self.limit:
                bot.send_message(message.chat.id, "Siz oz muddat ichida ko'p so'rov amalga oshirayapsiz❗")
                return CancelUpdate()
            self.last_time[message.from_user.id] = message.date

        def post_process(self, message, data, exception):
            pass

    bot.setup_middleware(SimpleMiddleware(0.86))
