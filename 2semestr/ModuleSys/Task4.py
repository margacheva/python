"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""
import sys
import os

put = sys.argv[1]
name = sys.argv[2]

os.system(f"mkdir {put}/{name}")
