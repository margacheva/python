"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""
from multiprocessing import Process


def even():
    n = 0
    for i in range(1, 1000001):
        if i % 2 == 0:
            n += i
    print(f"Сумма чётных чисел: {n}")


def odd():
    n = 0
    for i in range(1, 1000001):
        if i % 2 != 0:
            n += i
    print(f"Сумма нечётных чисел: {n}")


if __name__ == "__main__":
    p1 = Process(target=even)
    p1.start()

    p2 = Process(target=odd)
    p2.start()