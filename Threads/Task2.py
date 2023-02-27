"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import time
from threading import Thread


def reminder():
    rem = input('Напомнить: \n')
    seconds = int(input('через сколько секунд:\n'))
    time.sleep(seconds)
    print(rem)


th = Thread(target=reminder, daemon=True)
th.start()
time.sleep(10)
th.join()
print('Программа завершается')
