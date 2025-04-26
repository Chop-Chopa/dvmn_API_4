from dotenv import load_dotenv
import argparse
import telegram
import random
import time
import os


def send_photo_telegram(chat_id, token, filename):
    bot = telegram.Bot(token=token)
    with open(filename, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


def get_random_image_files():
    image_files = os.listdir('images')
    random.shuffle(image_files)
    return image_files


def main():
    load_dotenv()

    telegram_token = os.environ["TELEGRAM_TOKEN"]
    telegram_chat_id = os.environ["TG_CHAT_ID"]

    parser = argparse.ArgumentParser(description="Скрипт для автоматической публикации фото в Telegram.")
    parser.add_argument('--hours', type=int, default=int(os.environ["DELAY_HOURS"]), help="Задержка между публикациями в часах")
    parser.add_argument('--photo', type=str, help="Укажите фото для публикации (если не указано, публикуется случайное)")
    args = parser.parse_args()

    if args.photo:
        send_photo_telegram(telegram_chat_id, telegram_token, args.photo)
        return

    image_files = get_random_image_files()

    while True:
        if not image_files:
            image_files = get_random_image_files()

        photo_filename = image_files.pop(0)
        send_photo_telegram(telegram_chat_id, telegram_token, photo_filename)
        time.sleep(args.hours * 60 * 60)


if __name__ == '__main__':
    main()
