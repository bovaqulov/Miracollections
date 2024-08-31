from telebot.types import Message, ReplyKeyboardRemove
from telebot.util import split_string

from mirasite.settings import BOT_URL
from botapp.models import *

from botapp.bot.core.loader import bot
from botapp.bot.keywords.commands import *
from botapp.bot.keywords.inlines import *




def create_user(tg_id):
	TgUser.objects.create(tg_id=tg_id)


def reaction_start(tg_id):
	button = Button.objects.filter(title='/start').first()
	with open(f".{button.img.url}", "rb") as f :
		img = f.read()
	text = button.text
	bot.send_photo(tg_id, photo=img, caption=text, reply_markup=start_btn())

def reaction_connection(tg_id):
	button = Button.objects.filter(title="Aloqa ☎️").first()
	with open(f".{button.img.url}", "rb") as f :
		img = f.read()
	text = button.text
	bot.send_photo(tg_id, photo=img, caption=text, reply_markup=start_btn())

def reaction_design(tg_id):
	button = Button.objects.filter(title="Dezayinlar 🏠").first()
	with open(f".{button.img.url}", "rb") as f :
		img = f.read()
	text = button.text
	bot.send_photo(tg_id, photo=img, caption=text, reply_markup=design_btn())

def reaction_category(tg_id, cat_id):
	category = Category.objects.get(pk=pk)
	blinds = Blinds.objects.filter(category=category).order_by("-pk")

	blind = blinds.first()

	with open(f".{blind.img.url}", "rb") as f :
		img = f.read()
	text = blind.text

	bot.send_photo(tg_id, photo=img, caption=text, reply_markup=blinds_btn(blind.pk))
