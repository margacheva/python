"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл
где имя файла второй аргумент.
"""
import sys

text = sys.argv[2]
name = sys.argv[1]

file = open(name, 'w')
file.write(text)


