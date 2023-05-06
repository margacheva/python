"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов  всех персонажах начиная с вашего номера в журнале и заканчивая ваш номер*5
Сохраните в .json файл.
"""
import requests
import json

# Номер персонажа в журнале
start = 9
end = start * 5

# Отправляем GET-запрос на адрес https://rickandmortyapi.com/api/character/ и получаем данные о персонажах
r = requests.get(f"https://rickandmortyapi.com/api/character/{start},{end}")
data = r.json()

# Создаем список для хранения данных о персонажах
characters = []

# Обходим полученные данные и получаем нужные данные о каждом персонаже
for character in data["results"]:
    name = character["name"]
    planet = character["origin"]["name"]
    episodes = [episode.split("/")[-1] for episode in character["episode"]]
    characters.append({"name": name, "planet": planet, "episodes": episodes})

# Сохраняем полученные данные в .json файл
with open("characters.json", "w") as f:
    json.dump(characters, f)

