"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""
dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

ks = list(dict.keys())
vs = list(dict.values())

dict[ks[0]], dict[ks[-1]] = dict[ks[-1]], dict[ks[0]]
dict.pop(ks[1])
dict['new_key'] = 'new_value'

print(dict)