"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд)
если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""
import multiprocessing
import time


def check_subscription():
    while True:
        time.sleep(10)
        print("Ваша подписка закончилась.")
        break


def guess_number():
    number = 7
    while True:
        guess = int(input("Угадайте число от 1 до 10: "))
        if guess == number:
            print("Вы угадали!")
            break
        else:
            print("Неправильно, попробуйте еще раз.")


if __name__ == "__main__":
    p = multiprocessing.Process(target=check_subscription)
    p.start()
    guess_number()
    p.join()
