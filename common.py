from urllib.parse import urlparse
import os
import requests
import telegram
import random


def get_file_extension_from_url(url):
    path = urlparse(url).path
    return os.path.splitext(path)[1]


def save_image(url, file_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def message_telegram(chat_id, token):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")


def photo_telegram(chat_id, token):
    bot = telegram.Bot(token=token)
    filename = random.choice(os.listdir('images'))
    bot.send_document(chat_id=chat_id, document=open(f'images/{filename}', 'rb'))
