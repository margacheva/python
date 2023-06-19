"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""
from queue import Queue
from threading import Thread



def add_students(queue):
    while True:
        surname = input("Введите фамилию студента (или 'off' для завершения): ")
        if surname == "off":
            break
        queue.put(surname)


def expel_students(queue):
    while queue:
        surname = queue.get()
        print(f"Студент {surname} отчислен")


if __name__ == '__main__':
    queue = Queue()

    queue.put("Иванов")
    queue.put("Петров")
    queue.put("Сидоров")


    add_thread = Thread(target=add_students, args=(queue,))
    add_thread.start()
    expel_thread = Thread(target=expel_students, args=(queue,))

    expel_thread.start()


    add_thread.join()
    expel_thread.join()
