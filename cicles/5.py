price = ''
sale = ''
while True:
    price = int(input('Введите стоимость:'))
    sale = price - price / 10
    if price != 0:
        print('Стоимость с учетом скидки:', sale)
    else:
        print('Программа завершена.')
        break
