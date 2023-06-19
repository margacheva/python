import sys
from datetime import datetime
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import socket
from threading import Thread
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.82.85.235', 5501))
# Вписываем айпишник пк-сервера


class Enter(QMainWindow):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock
        uic.loadUi('login.ui', self)
        self.setWindowTitle('Chat')
        self.pushButton.clicked.connect(lambda: self.login())
        self.toolButton.clicked.connect(lambda: self.registration())
        # self.password_2.setReadOnly(True)

    # Обработчик события для кнопки "Войти в систему"
    def login(self):
        # Очистка поля пароля для сообщения об ошибке
        # self.lineEdit_3.setText('')
        # Получение введенных пользователем логина и пароля
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        # if username == "" or password == "":
        #     self.label.setText("Заполните все поля")
        #     return False
        # # Отправка кода операции (1 - вход в систему) на сервер
        sock.send("авт".encode())
        # # Очистка полей логина и пароля
        # self.lineEdit_2.setText('')
        # self.lineEdit_3.setText('')
        # Отправка логина и пароля на сервер
        sock.send(username.encode())
        sleep(0.1)
        sock.send(password.encode())
        # Получение ответа от сервера
        message = sock.recv(1024).decode()
        if message == "Good":
            self.close()
            sleep(0.5)
            exit = Chat(self.sock)
            exit.show()
        # users = sock.recv(1024).decode()
        # Если ответ сервера содержит "Успешно", закрытие текущего окна и открытие окна чата



    # Обработчик события для кнопки "Создать аккаунт"
    def registration(self):
        # Закрытие текущего окна и открытие окна регистрации
        self.close()
        exit = Registration(self.sock)
        exit.show()


class Registration(QMainWindow):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock
        uic.loadUi('registration.ui', self)
        self.setWindowTitle('Chat')
        self.pushButton.clicked.connect(lambda: self.registration_2())
        # self.password_2.setReadOnly(True)

        # Метод регистрации нового пользователя

    def registration_2(self):
        # Очищаем поле для ввода подтверждения пароля
        # self.lineEdit.setText('')
        # self.lineEdit_3.setText('')

        # Считываем введенные пользователем данные (логин, пароль, имя)
        name = self.lineEdit.text()
        password = self.lineEdit_3.text()
        # if name == "" or password == "":
        #     self.label_2.setText("Заполните все поля")
        #     return False
        # Отправляем на сервер сообщение о том, что это запрос на регистрацию
        sock.send("зар".encode())
        # Очищаем поля для ввода
        # self.lineEdit.setText('')
        # self.lineEdit_3.setText('')
        # self.label_2.setText('')
        # Отправляем на сервер введенные пользователем данные
        sock.send(name.encode())
        sleep(0.1)
        sock.send(password.encode())
        # Получаем ответ от сервера и выводим его в поле для ввода подтверждения пароля
        # response = sock.recv(1024).decode()
        # self.label_2.setText(response)
        # Если регистрация прошла успешно, закрываем окно регистрации и открываем окно входа
        # if "Good" in response:
        self.close()
        exit = Enter(self.sock)
        exit.show()


class Chat(QMainWindow):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Chat')
        self.pushButton.clicked.connect(lambda: self.send_message())
        self.textBrowser.setReadOnly(True)
        thread = Thread(target=self.get_message, daemon=True)
        thread.start()

    def get_message(self):
        while True:
            messages = sock.recv(1024).decode()
            sleep(0.1)
            if not messages:
                sleep(0.1)
                continue
            try:
                self.textBrowser.append(messages)
            except Exception as e:
                print(e)

    def send_message(self):
        message = self.lineEdit.text()
        sleep(0.1)
        data = datetime.now().strftime("%Y-%m-%d %H:%M")
        end = f"""{data}
{message}"""
        print(end)
        sock.send(end.encode('utf-8'))
        print("Я отправил ау")
        sleep(0.1)
        self.lineEdit.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exit = Enter(socket)
    exit.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        sock.send("Покидает чат".encode())
        print("...")
        sock.close()
