a = input('Введите число:')

if int(a[-1]) % 2 == 0 and sum(map(int, a.split())) % 3 == 0:
    print('yraaaa')
