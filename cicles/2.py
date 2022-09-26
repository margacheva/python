a = ''

while True:
    game = input('Введите "game" для игры, "off" для завершения: ')
    if game == 'game':
        for i in range(3):
            a = int(input('Введите число: '))
            if a == 5:
                break
            else:
                print('мимо, давай еще')

    elif game == 'off':
        print('конец игры')
        break
    else:
        print('что-то не понял')

    if a == 5:
        print('Вы выиграли билет на концерт!!')
        break