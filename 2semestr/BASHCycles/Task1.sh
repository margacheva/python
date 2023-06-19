#!/bin/bash
#Напишите скрипт который выводит все исполняемые файлы в системе

for file in /Users/yana/Desktop/Учеба/BashCourse/*
do
  if [ -x "$file" ]; then
    echo "Исполняемые файлы:"
    echo "$file"
    fi
done