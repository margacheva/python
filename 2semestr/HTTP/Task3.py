"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов  всех персонажах начиная с вашего номера в журнале и заканчивая ваш номер*5
Сохраните в .json файл.
"""
import json
import requests

characters_data = []

for i in range(12, 12 * 5 + 1):
    response = requests.get(f'https://rickandmortyapi.com/api/character/{i}')
    data = response.json()
    characters_data.append({
        'name': data['name'],
        'planet': data['origin']['name'],
        'episode': data['episode']
    })

with open('rick_and_morty.json', 'w') as f:
    json.dump(characters_data, f, indent=4)
print('done')