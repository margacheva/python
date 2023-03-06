"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""
from queue import Queue
from threading import Thread

students = Queue()


def get_students():
    surname = input("Surname")
    for i in range(len(surname)):
        if surname == 'off':
            return 'The end'
        else:
            students.put(surname)


def studentOff():
    print('Отчислен:', students.get())


def main():
    get_thread = Thread(
        target=get_students, args=(students,), daemon=True
    )
    get_thread.start()
    delete_thread = Thread(
        target=studentOff, args=(students,), daemon=True
    )
    delete_thread.start()
    get_thread.join()
    students.join()


print(main())
