m = [0, 2, 4, 6, 8, 10]
for i in range(len(m) - 1):
    n = m[1] - m[0]
    if m[i+1] - m[i] == n:
        continue
    else:
        a = 'НЕТ'
        print(a)
        break

if 'a' not in locals():
    print('ДА')






