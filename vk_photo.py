import json
import os
import pandas as pd
import requests
from pprint import pprint



class VK:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_photo(self, id):
        get_photo_url = self.url + 'photos.get'
        get_photo_params = {
            'owner_id': id,
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 1,
            'count': 5
        }
        req = requests.get(get_photo_url, params={**self.params, **get_photo_params}).json()['response']['items']
        vk_photo = []
        for photo in req:
            vk_photo.append({'likes': photo['likes']['count'], 'date_upload': photo['date'],
                            'link': photo['sizes'][-1], 'size': photo['sizes'][-1]['type']})

        photo_sort = sorted(vk_photo, key=lambda x: x['likes'])
        photo_dict = {}
        photo_list = []

        for photo in photo_sort:
            likes = photo['likes']
            size = photo['size']
            if f'{likes}.jpg' not in list(photo_dict.keys()):
                file_name = f'{likes}.jpg'
                photo_dict[file_name] = photo['link']
            else:
                rename = str(likes) + str(photo['date_upload'])
                file_name = f'{rename}.jpg'
                photo_dict[file_name] = photo['link']
            photo_list.append({'file_name': file_name, 'size': size})

        with open('photo.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(photo_list))
        for photo, link in photo_dict.items():
            image = requests.get(link['url'])
            full_file_name = os.path.join('vk', photo)
            with open(full_file_name, 'wb') as file:
                file.write(image.content)
        return print()


