import requests
import json
from pprint import pprint
from vk_photo import VK
from yandex_disk import YandexDisk
import os

with open('vk_token.txt', 'r', encoding='utf-8') as file:
    token_vk = file.read().strip()

id = input('введите id пользователя: ')

vk_client = VK(token_vk, '5.131')
vk_client.get_photo(id)

token_YD = input('введите токен яндекс диска: ')

my_file_path = r'vk'
y = YandexDisk(token_YD)
y.upload_photos(my_file_path)




