"""Напишите функцию генерирующую список из 100 случайных паролей из 8 символов
используя цифры и буквы.
Запустите функцию в отдельном процессе.
В основной части программы попросите у пользователя ввести пароль из 8 символов
и проверьте есть ли этот пароль в списке."""
from multiprocessing import Process
import random
import string

list_passwords = []


def passwords():
    for i in range(100):
        letters_and_numbers = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_numbers, 8))
        list_passwords.append(rand_string)
        print(rand_string)
    print(list_passwords)


passwords()
p1 = Process(target=passwords)
guess = ''
while True:
    guess = input('Угадайте пароль: ')
    if guess in list_passwords:
        print('Поздравляю, вы угадали пароль!')
        break
    else:
        print('Попробуйте еще разок...')
