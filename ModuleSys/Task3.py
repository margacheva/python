"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл
где имя файла второй аргумент.
"""
import sys
user_input = sys.stdin.readline()
spisok = []
for i in user_input:
    spisok.append(i)
file = open(spisok[1], 'w')
# with open('file', 'w') as f:
#     f.write(spisok[0])

