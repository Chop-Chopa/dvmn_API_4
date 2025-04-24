from dotenv import load_dotenv
from pathlib import Path
from common import save_image
import os
import requests


def fetch_epic_images(token, directory):
    payload = {
        "api_key": token
    }
    response = requests.get("https://api.nasa.gov/EPIC/api/natural", params=payload)
    response.raise_for_status()
    url_image_nasa = response.json()
    for image in range(len(url_image_nasa)):
        id_image = response.json()[image]["image"]
        earth_link = response.json()[image]["date"].split(" ")
        date = earth_link[0].split("-")
        url = "https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key=zIXSIafgWe5Tk0LmGZyx2yZXK7GieW12Xii7c78I".split("/")
        url[6:9]=date[0:3]
        new_url = '/'.join(url)
        nasa_url = new_url.replace("epic_1b_20190530011359", id_image)
        filename = f'earth_{image}.jpg'
        save_image(nasa_url, directory / filename)


def main():
    load_dotenv()

    nasa_acess_token = os.environ["NASA_TOKEN"]

    output_dir = Path('images')
    output_dir.mkdir(exist_ok=True)

    fetch_epic_images(nasa_acess_token, output_dir)


if __name__ == '__main__':
    main()