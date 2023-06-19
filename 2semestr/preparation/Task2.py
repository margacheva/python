""""Напишите функцию которая высчитывает факториал числа, запустите функцию в отдельном процессе.
В основной части программы запрашивайте числа пока пользователь не введет 0,
числа добавляются в кортеж.
После ввода 0 выведите сумму чисел в кортеже."""
from multiprocessing import *


def factorial():
    num = 1
    n = 10
    for i in range(2, n + 1):
        num *= i
    print(num)


if __name__ == '__main__':
    p1 = Process(target=factorial)
    p1.start()

tuple = []
x = ''
while x != 0:
    x = int(input('input number: '))
    tuple.append(x)

print(sum(tuple))
