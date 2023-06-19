"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""
import requests

# Отправляем GET-запрос на адрес https://randomuser.me/api/ и получаем данные о случайном пользователе
r = requests.get("https://randomuser.me/api/")
data = r.json()

# Получаем нужные данные из полученного ответа
name = data["results"][0]["name"]["first"]
country = data["results"][0]["location"]["country"]
phone = data["results"][0]["phone"]

# Выводим сообщение с полученными данными
print(f"Hi, I'm {name}, I'm from {country}, my phone number is {phone}")