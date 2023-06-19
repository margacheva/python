"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""

import time
from threading import Thread


def faster():
    while True:
        print('Вводите быстрее!!!')
        time.sleep(3)


th = Thread(target=faster, daemon=True)
th.start()
code = int(input('Введите код от бомбы: '))
if code == 1:
    print('Бомба разминирована')
else:
    print('Вы взорвались')
