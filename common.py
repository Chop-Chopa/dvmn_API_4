from urllib.parse import urlparse
import os
import requests

def get_file_extension_from_url(url):
    path = urlparse(url).path
    return os.path.splitext(path)[1]

def save_image(url, file_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)