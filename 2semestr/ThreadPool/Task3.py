"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""
import os
from queue import Queue
from threading import Thread

# Функция для создания пути к файлу
def create_path(name):
    path = os.path.join(os.getcwd(), f"{name}.txt") # Получаем текущую директорию и добавляем к ней имя файла с расширением .txt
    return path

# Функция для чтения имен из файла и добавления путей в очередь
def read_names(file_path, queue):
    with open(file_path, "r") as file: # Открываем файл на чтение
        for name in file:
            path = create_path(name.strip()) # Создаем путь к файлу и удаляем символы переноса строки
            queue.put(path) # Добавляем путь в очередь

# Функция для создания файлов
def create_file(queue):
    while not queue.empty(): # Пока очередь не пуста
        file_path = queue.get() # Получаем следующий путь из очереди
        with open(file_path, "w") as file: # Открываем файл на запись
            file.write("что-то написали в файлике") # Записываем текст в файл

if __name__ == '__main__':
    queue = Queue() # Создаем очередь
    read_thread = Thread(target=read_names, args=("Names.txt", queue)) # Создаем поток для чтения имен из файла и добавления путей в очередь
    write_threads = []
    for i in range(3): # Создаем 3 потока для создания файлов
        write_thread = Thread(target=create_file, args=(queue,))
        write_threads.append(write_thread)

    read_thread.start() # Запускаем поток чтения имен из файла
    for thread in write_threads:
        thread.start() # Запускаем потоки создания файлов

    read_thread.join() # Ожидаем завершения потока чтения имен из файла
    for thread in write_threads:
        thread.join() # Ожидаем завершения потоков создания файлов

    print("All files created successfully.") # Выводим сообщение о успешном создании файлов