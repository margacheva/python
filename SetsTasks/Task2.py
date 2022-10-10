"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False. И изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""
testList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]

m = []
hashable = [int, float, tuple, bool, str, bytes]
counter = 0
for e in testList:
    if type(e) in hashable:
        counter += 1
    else:
        m.append(e)

if counter == len(testList):
    print(True)
else:
    print(False)
    print(m)
