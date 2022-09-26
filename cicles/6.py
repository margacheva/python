price = ''
counter = 0
while True:
    if price == 0:
        break
    price = int(input('Введите цену товара: '))
    counter += price

if counter % 2 == 0:
    while counter % 2 == 0:
        counter = int(counter / 2)
    print('К оплате:', counter)
else:
    print('К оплате:', counter - counter / 15)
