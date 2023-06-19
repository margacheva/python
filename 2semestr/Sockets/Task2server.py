"""
Разработайте приложение, которое будет запрашивать у пользователя название файла,
а затем отправлять содержимое этого файла серверу. Сервер будет выводить сообщение, подсчитывать количество слов и возвращать ответ.
Протестируйте на test.txt
"""
import socket

# создаем сокет для подключения к серверу
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# привязываем сокет к адресу и порту
sock.bind(("localhost", 5055))

# начинаем прослушивание подключений, максимальное количество клиентов - 10
sock.listen()

# ждем подключения клиента и выводим информацию о подключении
conn, addr = sock.accept()
print(f"Подключен: {addr}")
while True:
    recv = conn.recv(1024).decode()
    if recv != "off":
        file = open(recv)
        words = 0
        for line in file:
            words += len(line.split())
        conn.send(bytes(f"Ваш файл содержит: {words} слов", encoding="UTF-8"))
        print("Ответ отправлен")
    else:
        break

conn.close()
