review = ' '

while True:
    review = input('Введите отзыв: ').lower()
    if review == 'off':
        print('Система предпочтений настроена.')
        break
    else:
        print('Cпасибо, ваш отзыв принят!')
