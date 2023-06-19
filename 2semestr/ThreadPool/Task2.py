"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""
from queue import Queue
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from time import sleep

# функция для вывода всех делителей числа
def print_divisors(num):
    print(f"Делители числа {num}:")
    for i in range(1, num+1):
        if num % i == 0:
            print(i)


if __name__ == '__main__':
    queue = Queue() # создаем очередь для чисел

    # добавляем числа в очередь
    queue.put(10)
    queue.put(20)
    queue.put(30)

    # запускаем функцию в пуле потоков
    with ThreadPoolExecutor(max_workers=2) as executor:
        while not queue.empty():
            num = queue.get()
            executor.submit(print_divisors, num)
            sleep(2)