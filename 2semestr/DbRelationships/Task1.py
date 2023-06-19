"""
Создайте модели базы данных с отношением 1 ко многим.
Читатель содержит столбцы : id,имя, список книг
Книга содержит столбцы: id,Название, автор.
1 читатель может иметь много книг.
Напишите функцию вывода всех книг для вводимого с клавиатуры читателя.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Session

# строка подключения
sqlite_database = "sqlite:///books.db"
# создаем движок SqlAlchemy
engine = create_engine(sqlite_database)


# СОЗДaeм базовый класс для моделей
class Base(DeclarativeBase): pass


# Создаем модель, объекты которой будут храниться в бд
class Reader(Base):
    __tablename__ = "reader"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    book_id = Column(Integer, ForeignKey('book.id'))
    book_list = relationship("Book", back_populates="readers")


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    author = Column(String, )
    readers = relationship("Reader", back_populates="book_list")


# создаем таблицы
Base.metadata.create_all(bind=engine)


def create():
    with Session(autoflush=False, bind=engine) as db:
        book1 = Book(name='Унесённые ветром', author='Маргарет Митчелл')
        book2 = Book(name='Сто лет одиночества', author='Габриэль Гарсия Маркес')
        book3 = Book(name='Великий Гэтсби', author='Фрэнсис Скотт Фитцджеральд')
        yana = Reader(name='Yana')
        olga = Reader(name='Olga')
        elena = Reader(name='Elena')
        book1.readers = [yana, olga]
        book2.readers = [yana, elena]
        book3.readers = [olga, elena]
        db.add_all([book1, book2, book3])
        db.commit()
    print('Читатели и книги успешно добавлены')


def get_books_by_user():
    with Session(autoflush=False, bind=engine) as db:
        name_inp = input('Введите читателя: ')
        reader = db.query(Reader).filter(Reader.name == name_inp).all()
        for i in reader:
            print(f"Все книги читателя {i.name}")
            for j in i.book_list:
                print(j.name)
#             не выводит список книг


get_books_by_user()
