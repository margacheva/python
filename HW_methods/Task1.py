"""
 Создайте класс Person у которого будут свойства name и age.
 Добавьте метод экземпляра который выводит информацию о человеке.
 Создайте метод класса который генерирует новый объект класса
 который ставить возраст человека: сегодняшний год - год который передают в метод.
 (подсказка: тут можно использовать метод today().year класса date из модуля datetime)
 Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
 """
from datetime import date


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

    @classmethod
    def new_person(cls, year):
        return Person('Oleg', date.today().year - year)

    @staticmethod
    def pivo(self):
        if self.age >= 18:
            print('Yes')
        else:
            print('No')
Oleg = Person("oleg1",24)
new_oleg = Person.new_person(1998)
another_oleg =  Person.new_person(1996)
Oleg.info()
new_oleg.info()
another_oleg.info()
