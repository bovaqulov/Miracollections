import pyautogui
import random
import pyperclip

emj = ["❤️", "🧡", "🥰", "😘",
    "💛", "💚", "💙", "💜",
    "🖤", "💞", "❣️", "💓",
    "💗", "💖", "💘", "💝"]

def send_random_emoji():
    random_emoji = random.choice(emj)
    pyperclip.copy(random_emoji)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')


while True:
    send_random_emoji()
