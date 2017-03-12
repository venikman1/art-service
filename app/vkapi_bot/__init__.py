from config import *
import vk
import requests

def post(desription, images, date):
    upload_images = save(images, desription)
    images_attachment = []
    for i in upload_images:
        images_attachment.append(i['id'])
    images_attachment = ','.join(images_attachment)
    vk_client.wall.post(owner_id=group_id, from_group=1, message=desription, attachments=images_attachment, publish_date=date)


def save(file_names, description):
    upload_url = vk_client.photos.getUploadServer(album_id=album_id)['upload_url']

    files = {}
    for i in range(len(file_names)):
        files[u"file" + str(i + 1).encode('utf-8')] = open(file_names[i], "rb")
    r = requests.post(upload_url, files=files)
    r = r.json()
    #print (r)
    #print (files)
    return vk_client.photos.save(album_id=album_id, server=r['server'], photos_list=r['photos_list'], hash=r['hash'], caption=description)