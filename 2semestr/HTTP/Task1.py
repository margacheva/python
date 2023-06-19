"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""
import requests

def save_cat_images():
    # Получаем ссылки на картинки случайных котиков
    response = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png&limit=2')
    cat_links = [cat['url'] for cat in response.json()]

    # Сохраняем 2 картинки случайных котиков
    for i in range(2):
        response = requests.get(cat_links[i])
        with open(f'cat{i+1}.jpg', 'wb') as f:
            f.write(response.content)

    # Получаем ссылки на оригинальные картинки
    headers = {'x-api-key': 'YOUR_API_KEY'}
    response = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png&limit=2&category_ids=5', headers=headers)
    original_links = [cat['url'] for cat in response.json()]

    # Сохраняем 2 оригинальные картинки
    for i in range(2):
        response = requests.get(original_links[i])
        with open(f'original{i+1}.jpg', 'wb') as f:
            f.write(response.content)

    # Получаем ссылки на пиксельные картинки
    response = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=png&limit=2&category_ids=4', headers=headers)
    pixel_links = [cat['url'] for cat in response.json()]

    # Сохраняем 2 пиксельные картинки
    for i in range(2):
        response = requests.get(pixel_links[i])
        with open(f'pixel{i+1}.png', 'wb') as f:
            f.write(response.content)
