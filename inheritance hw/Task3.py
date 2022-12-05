"""
 Создайте класс SpaceObject у которого будут свойство размер.
 Создайте 2 класса Star и Planet которые будут наследовать SpaceObject.
  В классе Star добавьте свойство яркость
 и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
 Классу Planet добавьте свойства население и прирост за год и метод
 который будет печатать население через переданное
 ему количество лет.
 """


class SpaceObject():
    def __init__(self, size):
        self.size = size


class Star(SpaceObject):
    def __init__(self, size, light):
        super().__init__(light)
        self.light = light

    def to_light(self):
        print(self.light)


class Planet(SpaceObject):
    def __init__(self, size, light, population, plus_people):
        super().__init__(population)
        super().__init__(plus_people)
        self.population = population
        self.plus_people = plus_people

    def years(self, year):
        print(self.population + (year * self.plus_people))


sun = Star(123, 555)
Earth = Planet(111, 222, 1, 5)
Earth.years(5)
