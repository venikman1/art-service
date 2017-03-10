import vk
import requests
from config import *


def save(file_names, description):
    upload_url = vk_client.photos.getUploadServer(album_id=album_id)['upload_url']
    files = {}
    for i in range(len(file_names)):
        files["file" + str(i + 1)] = open(file_names[i], "rb")
    r = requests.post(upload_url, files=files)
    r = r.json()
    return vk_client.photos.save(album_id=album_id, server=r['server'], photos_list=r['photos_list'], hash=r['hash'], caption=description)