""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""
import os
os.mkdir(r'/Users/yana/Desktop/task4')
with open('/Users/yana/Desktop/task4/answer.txt','w') as f:
    f.write('я выполнил задание')