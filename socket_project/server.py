# Создаем хоста для мессенджера. Этот хост использует локальный айпишник получаемый через ipconfig.
# Когда пользователь запускает код клиента он регистрируется через хост этого пк(при этом все что необходимо иметь пользователю это код клиента и находиться в одной сети с хостом).

import socket
import client_database
from threading import Thread

# hostname = socket.gethostname()
# localip = socket.gethostbyname(hostname)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.82.85.235', 5501))  # Привязываем сервер к локальному айпишнику. Важно проверять его через ipconfig перед запуском хоста.
sock.listen(10)
print('Сервер запущен')

users = []  # Создаем список пользователей.

client_sockets = set() # Переменная в которой мы храним сокеты пользователей.


def reciver(
        cs):  # Регистрация и авторизация пользователя происсходит здесь. Пользователь выходит из цикла только когда авторизуется.
    while True:
        start = cs.recv(1024).decode()
        if 'зар' in start.lower():
            name = cs.recv(1024).decode()
            password = cs.recv(1024).decode()
            print(name, password)
            if not client_database.create(name, password):
                sock.send("yes".encode())
                continue
        elif 'авт' in start.lower():
            name = cs.recv(1024).decode()
            password = cs.recv(1024).decode()
            print(name)
            print(password)
            rtn = client_database.authenticate(name, password)
            print(rtn)
            if rtn:
                print(1)
                if name not in users:
                    print(2)
                    users.append(name)
                else:
                    print(3)
                    cs.send((str('Bad').encode()))
                    # cs.send((str('Bad').encode()))
                    continue
                users_to_send = ' '.join(users)
                cs.send('Good'.encode())
                print("WIN")
                th = Thread(target=send,args=(cs,)).start()
                # cs.send(str(users).encode())
                break
            else:
                print("BAD")
                cs.send((str('Bad').encode()))
                # cs.send((str('Bad').encode()))



def send(cs):
    while True:  # Через этот цикл мы посылаем всем пользователям сообщения.
        try:
            msg = cs.recv(1024).decode()  # <-Вот тут принимает.
            print(msg)
        except:  # Здесь мы проверяем не отключился ли какой-нибудь пользователь. Если кто-нибудь отключился мы зарзываем с ним соединение.
            client_sockets.remove(cs)
            cs.close()
            break
        else:
            print(client_sockets)
            for i in client_sockets:  # Вот тут с рассылкаем всем подключенным пользователям.
                i.send(msg.encode())


while True:  # Множество в котором храним список пользователей.
    conn, addr = sock.accept()
    print('connected: ', addr)
    # data = conn.recv(1024)
    # print(str(data))
    client_sockets.add(conn)  # Функцией добавляем в список нового пользователя.

    thread1 = Thread(target=reciver, args=(conn,), daemon=True)
    thread1.start()