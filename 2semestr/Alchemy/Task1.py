"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов,
получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

# строка подключения
sqlite_database = "sqlite:///task1.db"
# создаем движок SqlAlchemy
engine = create_engine(sqlite_database)


# СОЗДaeм базовый класс для моделей
class Base(DeclarativeBase): pass


# Создаем модель, объекты которой будут храниться в бд
class Films(Base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    year = Column(Integer, )
    kind = Column(String)
    rating = Column(Float)


# создаем таблицы
Base.metadata.create_all(bind=engine)


def create_film():
    with Session(autoflush=False, bind=engine) as db:
        New_film = Films(name='Титаник', year=2004, kind='Драма', rating=7.0)
        db.add(New_film)
        db.commit()
    print(f'Фильм  успешно добавлен')


def get_all_films():
    with Session(autoflush=False, bind=engine) as db:
        films = db.query(Films).all()
        for i in films:
            print(i.name)


def get_film_by_year():
    with Session(autoflush=False, bind=engine) as db:
        films = db.query(Films).filter(Films.year == 2004).all()
        for i in films:
            print(i.name)


def update_rating():
    with Session(autoflush=False, bind=engine) as db:
        titanic = db.query(Films).filter(Films.id == 1).first()
        titanic.rating = 2.0
        db.commit()
        print('рейтинг изменен')


def delete_films():
    with Session(autoflush=False, bind=engine) as db:
        titanic = db.query(Films).filter(Films.name == 'Титаник').first()
        db.delete(titanic)
        db.commit()
        print('фильм удален')


delete_films()
