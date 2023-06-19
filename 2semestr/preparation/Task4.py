"""Напишите функцию, предлагающую пользователю ввести пароль
пока пользователь не введет “off” и выводящую информацию о его надежности.
Надежным считается пароль, в котором больше 8 символов и есть хотя бы 1 буква в верхнем регистре.
Запустите функцию в отдельном потоке. Напишите функцию которая считает факториал числа 100000.
Запустите функцию в отдельном потоке, но только тогда когда пользователь закончит вводить пароли."""
from threading import Thread


def password():
    password = ''
    while password != 'off':
        password = input('Введите пароль: ')
        if len(password) < 8:
            print('Ваш пароль ненадежный')
        elif len(password) >= 8 and password.islower() == False:
            print('Ваш пароль надежный')


def factorial():
    num = 1
    n = 100
    for i in range(2, n + 1):
        num *= i
    print(num)


if __name__ == '__main__':
    thread1 = Thread(target=password)
    thread2 = Thread(target=factorial)
    thread1.start()
    thread1.join()
    thread2.start()
