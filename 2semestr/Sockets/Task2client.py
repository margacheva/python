import socket

# создаем сокет для подключения к серверу
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# устанавливаем соединение с сервером
sock.connect(("localhost", 5055))

while True:
    mssg = input("Введите название файла: ")
    if mssg == "off":
        break
    else:
        sock.send(bytes(mssg, encoding="UTF-8"))
    recv = sock.recv(1024).decode()
    print(recv)

sock.close()
