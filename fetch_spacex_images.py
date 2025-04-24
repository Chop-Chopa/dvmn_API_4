from pathlib import Path
from common import save_image
import argparse
import requests


def fetch_spacex_images(launch_id, directory):
    if launch_id:
        url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    else:
        url = "https://api.spacexdata.com/v5/launches/latest"

    response = requests.get(url)
    response.raise_for_status()

    image_urls = response.json()['links']['flickr']['original']
    for index, img_url in enumerate(image_urls):
        filename = f"spacex_{index}.jpg"
        save_image(img_url, directory / filename)


def main():
    parser = argparse.ArgumentParser(description="Скачиваний фотографий SpaceX")
    parser.add_argument('launch_id', help='Идентификатор запуска')
    args = parser.parse_args()

    output_dir = Path("images")
    output_dir.mkdir(exist_ok=True)

    fetch_spacex_images(args.launch_id, output_dir)


if __name__ == '__main__':
    main()
