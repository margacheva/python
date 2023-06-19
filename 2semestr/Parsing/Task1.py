"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучите источник, посмотрите как именно на сайт приходит информация.
Сохраните данные в json файл в формате:
{
место в чарте: (исполнитель,трек)
}
"""
import requests
from bs4 import BeautifulSoup
import json


def yandex_chart(url):
    r = requests.get(url)
    page = BeautifulSoup(r.text, 'lxml')

    singer = page.findAll('div', attrs={'class': 'd-track__meta'})

    track = page.findAll('div', attrs={'class': 'd-track__name'})

    res = {i + 1: {singer[i].text: ' '.join(track[i].text.split())}
           for i in range(len(track))}

    with open('chart1.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False)

yandex_chart("https://music.yandex.ru/chart")
print("done")
