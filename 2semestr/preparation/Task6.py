from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

# строка подключения
sqlite_database = "sqlite:///prep5.db"
# создаем движок SqlAlchemy
engine = create_engine(sqlite_database)


# СОЗДaeм базовый класс для моделей
class Base(DeclarativeBase): pass


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


Base.metadata.create_all(bind=engine)
db = Session(autoflush=False, bind=engine)
