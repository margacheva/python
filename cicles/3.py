login = input('Введите логин: ')
m = ['=', '*', '^', '$', '№', '@', '_']
ban = ''

for i in login:
    if i in m:
        ban += i
if ban == '':
    print('нет запрещенных элементов')

print(ban)
