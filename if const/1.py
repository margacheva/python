price1 = int(input())

price2 = int(input())

price3 = int(input())

if price1 < price2 < price3:
    print('Акция!', (price1 + price2 + price3) / 2)

elif price1 > price2 > price3:
    print('Акция!',(price1 + price2 + price3) / 3)

else:
    print('К оплате:', (price1 + price2 + price3))

