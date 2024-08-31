from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import telebot
import os

from botapp.bot.core.loader import bot, middle

import botapp.bot.handlers

middle()

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


