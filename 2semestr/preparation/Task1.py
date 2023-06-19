"""Напишите функцию которая с периодичностью в 2 секунды записывает в файл числа от 0 до 100 с шагом 3.
Запустите функцию в потоке демоне, в основном потоке напишите бесконечный цикл
который запрашивает у пользователя фамилии и заносит в список.
Если введено слово off выводится список фамилий."""
from threading import Thread
import time


def numbers():
    for i in range(0, 100, 3):
        with open("numbers.txt", "a+") as file:
            file.write(str(i) + "\n")
            time.sleep(2)


thread = Thread(target=numbers, daemon=True)
thread.start()

list_name = []
name = ''
while name != "off":
    name = input("Input name: ")
    list_name.append(name)
print(list_name)
