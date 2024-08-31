from telebot.types import CallbackQuery, ReplyKeyboardRemove

from botapp.bot.core.loader import bot
from botapp.bot.keywords.commands import *

from .utils import *



class UserInlineHandler:
    def __init__(self, call: CallbackQuery):
        self.call = call

    def manager(self):
        chat_id = self.call.message.chat.id
        msg_id = self.call.message.id
        data = self.call.data
        call = self.call

        

@bot.callback_query_handler(func=lambda call: call.data == call.data)
def user_inlines(call: CallbackQuery):
    try:
        UserInlineHandler(call).manager()
    except Exception as e:
        print(f'ERROR: handlers/users/callback.py --> {e}')
