"""
Напишите скрипт который в качестве параметра из командной строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""
import os
import sys

name = sys.argv[1]

with open(name, 'r') as file:
    commands = file.readlines()

for i in commands:
    os.system(i)