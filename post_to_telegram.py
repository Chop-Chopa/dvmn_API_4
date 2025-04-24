from dotenv import load_dotenv
import argparse
import telegram
import random
import time
import os


def message_photo(chat_id, token, filename):
    bot = telegram.Bot(token=token)
    bot.send_document(chat_id=chat_id, document=open(f'images/{filename}', 'rb'))


def main():
    load_dotenv()

    telegram_token = os.environ["TELEGRAM_TOKEN"]
    telegram_chat_id = os.environ["TG_CHAT_ID"]

    parser = argparse.ArgumentParser(description="Скрипт для автоматической публикации фото в Telegram.")
    parser.add_argument('hours', type=int, default=int(os.environ["DELAY_HOURS"]), help="Задержка между публикациями в часах")
    args = parser.parse_args()

    image_files = [image for image in os.listdir('images')]
    random.shuffle(image_files)

    while True:
        if not image_files:
            image_files = [image for image in os.listdir('images')]
            random.shuffle(image_files)

        photo_filename = image_files.pop(0)
        message_photo(telegram_chat_id,telegram_token,photo_filename)
        time.sleep(args.hours * 60 * 60)


if __name__ == '__main__':
    main()
