from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash,check_password_hash

sqlite_database = 'sqlite:///persons.db'
engine = create_engine(sqlite_database)
class Base(DeclarativeBase): pass
class Persons(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)

Base.metadata.create_all(bind=engine)

db = Session(autoflush=False, bind=engine)

def init():

    # Создаем объекты модели данных для начальных записей
    user_1 = Persons(name="Яна", password=generate_password_hash("123", "sha256"))
    user_2 = Persons(name="123", password=generate_password_hash("123", "sha256"))
    list_1 = [user_1, user_2]
    # Добавляем объекты в сессию ORM и фиксируем изменения в базе данных
    db.add_all(list_1)
    db.commit()

def create(usr_name, usr_passwrd):
    with Session(autoflush=False, bind=engine) as db:
        # Проверяем, есть ли пользователь с таким именем
        existing_user = db.query(Persons).filter_by(name=usr_name).first()
        if existing_user:
            print('Пользователь с таким именем уже существует.')
        else:
            person = Persons(name=usr_name, password=generate_password_hash(usr_passwrd, "sha256"))
            db.add(person)
            db.commit()
            return existing_user


def authenticate(usr_name, usr_passwrd):
    with Session(autoflush=False, bind=engine) as db:
        existing_user = db.query(Persons).filter_by(name=usr_name).first()
        if existing_user and check_password_hash(existing_user.password, usr_passwrd):
            return True
        else:
            return False



def all_persons():
    with Session(autoflush=False, bind=engine) as db:
        all_usrs = db.query(Persons)
        for k in all_usrs:
            print(f'{k.name}, {k.password}')

if __name__ == '__main__':
    all_persons()
