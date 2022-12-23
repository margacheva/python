"""
Создайте классы утка и человек. У обоих классов нету свойств,
но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье.
Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""
class Duck():
    def ducking(self):
        print('quack quack')
    def wear_cloths(self):
        print('I do not wear anything')
class Human():
    def ducking(self):
        print('I cannot make quack quack')
    def wear_cloths(self):
        print('I wear t-shirt and jeans')

duck = Duck()
Yana = Human()
for e in(duck, Yana):
    e.ducking()
    e.wear_cloths()