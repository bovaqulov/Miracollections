from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from .command_list import *


def start_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    markup.row(
    	KeyboardButton(start_command[0]), 
    	KeyboardButton(start_command[1]))

    return markup


def design_btn():
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

	markup.row(
		KeyboardButton(designs_btn[0]), 
		KeyboardButton(designs_btn[1]))

	markup.row(
		KeyboardButton(designs_btn[2]), 
		KeyboardButton(designs_btn[3]))

	markup.row(
		KeyboardButton(designs_btn[4]))

	return markup