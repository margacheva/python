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
    stop = ''
    while stop != 1:
        stop = input('Введите ентер чтобы начать или 1 чтобы закончить: ')
        info = []
        film_name = input('Введите название фильма:')
        info.append(film_name)
        film_year = input('Введите год выпуска фильма:')
        info.append(film_year)
        film_kind = input('Введите жанр фильма:')
        info.append(film_kind)
        film_rating = input('Введите рейтинг фильма:')
        info.append(film_rating)
        with Session(autoflush=False, bind=engine) as db:
            New_film = Films(name=info[0], year=info[1], kind=info[2], rating=info[3])
            db.add(New_film)
            db.commit()
        print('Пользователь успешно добавлен')
        info.clear()



