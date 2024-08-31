from telebot.types import Message
from pprint import pprint

from botapp.bot.core.loader import bot
from botapp.models import *
from .utils import *



class UserTextHandlers:
	def __init__(self, msg):
		self.msg = msg

	def manager(self):

		chat_id = self.msg.chat.id
		msg_id = self.msg.id	
		user_text = self.msg.text
		username = self.msg.from_user.username,
		first_name = self.msg.from_user.first_name

		create_user(chat_id)

		if '/start' == user_text:
			reaction_start(chat_id)
			return

		if "Aloqa ☎️" == user_text:
			reaction_connection(chat_id)
			return

		if "Dezayinlar 🏠" == user_text:
			reaction_design(chat_id)
			return

		if "Ortga" == user_text:
			reaction_start(chat_id)
			return

		if user_text in [c.title for c in Category.objects.all()]:
			cat_id = Category.objects.get(title=user_text).pk
			reaction_category(chat_id, cat_id)
			return



@bot.message_handler(content_types=["text"])
def user_text_handler(msg: Message):
	try:
		UserTextHandlers(msg).manager()
	except Exception as ex:
		print("Error: {}".format(ex))
