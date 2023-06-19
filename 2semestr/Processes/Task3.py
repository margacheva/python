"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""
from multiprocessing import Process, Pipe
import time

# функция для вычисления валюты
def calculate_currency(pipe, amount):
    currency = amount // 75 # делим сумму на курс валюты
    pipe.send(currency) # отправляем результат в родительский процесс

if __name__ == '__main__':
    parent_conn, child_conn = Pipe() # создаем конвейер между родительским и дочерним процессами
    amounts = [1000, 500, 2000, 750, 1500]

    processes = []
    for amount in amounts:
        p = Process(target=calculate_currency, args=(child_conn, amount)) # создаем дочерний процесс для каждой суммы
        p.start()
        processes.append(p)

        time.sleep(0.5)

    for i in range(len(amounts)):
        print(f"Количество: {amounts[i]}, После обмена: {parent_conn.recv()}") # получаем результаты из конвейера и выводим их на экран

    for p in processes:
        p.join() # ждем завершения всех дочерних процессов перед завершением родительского процесса