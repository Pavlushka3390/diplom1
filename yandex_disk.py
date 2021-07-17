from pprint import pprint
import requests
import os
import json


class YandexDisk:

    def __init__(self, token):
        self.token = token
        self.headers_Ya = {'Accept': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def upload_photos(self, path):
        self.path = path
        file_list = os.listdir(self.path)
        path_list = []
        for file in file_list:
            path = os.path.join(self.path, file)
            path_list.append(path)
        requests.put('https://cloud-api.yandex.net/v1/disk/resources?path=%2Fvk', headers=self.headers_Ya)
        for i, path1 in enumerate(path_list, 1):
            with open(path1, 'rb') as f:
                _file = f.read()

            response = requests.get(
                f'https://cloud-api.yandex.net/v1/disk/resources/upload?path=%2Fvk/{os.path.basename(path1)}',
                headers=self.headers_Ya).json()
            print(response)
            link_upload = response['href']
            operation_id = response['operation_id']
            requests.put(link_upload, headers=self.headers_Ya, data=_file)
            while True:
                status = requests.get(f'https://cloud-api.yandex.net/v1/disk/operations/{operation_id}',
                                      headers=self.headers_Ya).json()['status']
                if status == 'success':
                    break
            print(f'Изображение "{os.path.basename(path1)}" {str(i)}/{str(len(path_list))} загружено на диск')
        print()
        return print('Все изображения загружены')