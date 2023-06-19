"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""
import os
import threading
import time

# Создаем функцию для замены "ids" на "id"
def replace_ids(file_path):
    # Открываем файл для чтения
    with open(file_path, 'r') as f:
        content = f.read()
    # Заменяем "ids" на "id"
    content = content.replace('ids', 'id')
    # Открываем файл для записи и сохраняем изменения
    with open(file_path, 'w') as f:
        f.write(content)

# Запускаем таймер
start_time = time.time()

# Получаем список файлов в папке files
files = os.listdir('files')
threads = []

# Для каждого файла создаем поток и запускаем функцию replace_ids
for file in files:
    file_path = os.path.join('files', file)
    thread = threading.Thread(target=replace_ids, args=(file_path,))
    threads.append(thread)
    thread.start()

# Ждем завершения всех потоков
for thread in threads:
    thread.join()

# Останавливаем таймер и выводим время выполнения программы
end_time = time.time()
print(f'Программа выполнилась за {end_time - start_time} seconds')


