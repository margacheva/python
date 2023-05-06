"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучите источник, посмотрите как именно на сайт приходит информация.
Сохраните данные в json файл в формате:
{
место в чарте: (исполнитель,трек)
}
"""
import requests
import json

# Отправляем GET-запрос на адрес https://music.yandex.ru/chart и получаем данные о чарте
r = requests.get("https://music.yandex.ru/chart")
data = r.json()

# Создаем список для хранения данных о треках
tracks = []

# Обходим полученные данные и получаем нужные данные о каждом треке
for i, track in enumerate(data["tracks"]):
    artist = track["artists"][0]["name"]
    name = track["title"]
    tracks.append({i+1: (artist, name)})

# Сохраняем полученные данные в .json файл
with open("chart.json", "w") as f:
    json.dump(tracks, f)
