room = int(input())
street = int(input())

if street > room:

    if room > 20:
        print('on')

    elif room <= 20:
        print('off')

else:
    print('open window')
