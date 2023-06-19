"""
Создайте базу данных пользователя состояющую из следующих столбцов: id,username,password(В виде хэша).
Создайте программу которая предлагает пользователю зарегистрироваться или авторизироваться.
При регистрации программа запрашивает логин и пароль и добавляет в базу данных нового пользователя.
При авторизации программа запрашивает логин и пароль и выводит сообщение об успешной/неуспешной авторизации.
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash,check_password_hash

# строка подключения
sqlite_database = "sqlite:///users.db"
# создаем движок SqlAlchemy
engine = create_engine(sqlite_database)


# СОЗДaeм базовый класс для моделей
class Base(DeclarativeBase): pass


# Создаем модель, объекты которой будут храниться в бд
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)


# создаем таблицы
Base.metadata.create_all(bind=engine)


def auth():
    while True:
        question = int(input('Введите 1, если хотите зарегистрироваться и 2, если хотите авторизоваться и 3, если хотите выйти'))
        if question == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            with Session(autoflush=False, bind=engine) as db:
                new_user = Users(username=login, password=generate_password_hash(password, 'sha256'))
                db.add(new_user)
                db.commit()
            print(f'Пользователь {login} успешно зарегистрирован')
        if question == 2:
            while True:
                login = input('Введите логин: ')
                password = input('Введите пароль: ')
                with Session(autoflush=False, bind=engine) as db:
                    user = db.query(Users).filter(Users.username == login).first()
                    if login == user.username and check_password_hash(user.password,password):
                        print("Вы успешно авторизованы")
                        break
                    elif login != user.username:
                        print("Неверный логин")
                    elif not check_password_hash(password, user.password):
                        print("Неверный пароль")
                    else:
                        print("Такого пользователя не существует")
auth()






