"""
Создайте модели базы данных работников it-компании
Таблица Работники содержит следующие столбцы: id,имя,стаж, должности
Таблица Должности содержит следующие столбцы: id, название, работники.
Напишите функции вывода всех должностей запрашиваемого работника, всех работников по должности, всех работников определенной должности со стажем больше 5.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Session

# строка подключения
sqlite_database = "sqlite:///workers.db"
# создаем движок SqlAlchemy
engine = create_engine(sqlite_database)


# СОЗДaeм базовый класс для моделей
class Base(DeclarativeBase): pass


association_table = Table('association', Base.metadata,
                          Column('position_id', Integer, ForeignKey('positions.id')),
                          Column('worker_id', Integer, ForeignKey('worker.id')))


class Positions(Base):
    __tablename__ = "positions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    workers = relationship("Workers", secondary=association_table,back_populates="positions")


# Создаем модель, объекты которой будут храниться в бд
class Workers(Base):
    __tablename__ = "worker"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    experience = Column(Integer)
    positions = relationship("Positions",secondary=association_table,back_populates="workers")


Base.metadata.create_all(bind=engine)


def create():
    with Session(autoflush=False, bind=engine) as db:
        position1 = Positions(name="Стажер")
        position2 = Positions(name="Директор")
        position3 = Positions(name="Официант")
        yana = Workers(name="Яна", experience=10)
        oleg = Workers(name="Олег", experience=1)
        elena = Workers(name="Елена", experience=3)
        position1.workers = [oleg, yana]
        position2.workers = [yana, elena]
        position3.workers = [elena, oleg]
        db.add_all([position1, position2, position3])
        db.commit()


def all_positions():
    with Session(autoflush=False, bind=engine) as db:
        work = db.query(Workers).filter(Workers.name == "Яна").first()
        for j in work.positions:
            print(j.name)


def all_workers():
    with Session(autoflush=False, bind=engine) as db:
        work = db.query(Workers).filter(Workers.position == "").first()
        for i in work:
            print(i.workers)


def all_workers_5():
    with Session(autoflush=False, bind=engine) as db:
        worker = db.query(Workers).filter(Workers.position == "" and Workers.experience > 5).first()
        for i in worker:
            print(i.name)

create()
all_positions()
