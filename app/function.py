import vk
from config import *
from photo_save import save


def post(desription, images, date):
    upload_images = save(images, desription)
    images_attachment = []
    for i in upload_images:
        images_attachment.append(i['id'])
    images_attachment = ','.join(images_attachment)
    vk_client.wall.post(owner_id=group_id, from_group=1, message=desription, attachments=images_attachment, publish_date=date)