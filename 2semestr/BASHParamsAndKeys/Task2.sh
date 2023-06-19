#!/bin/bash
#Напишите скрипт который выводит надпись "Привет мир" если не было передано никаких аргументов.
#Если 1 из аргументов "-n" то следующий аргумент должен быть имя. В таком случае выведите надпись "Привет {Имя}"
#Пример ввода: myskript kakoitoArgument -n Oleg(Скрипт должен напечатать привет Oleg)
count=0

if [ $# -eq 0 ]; then
  echo "Hello, World!"
else
  for param in "$@"; do
    if [ "$param" == "-n" ]; then
      echo "Hello ${@:((count+2)):1}"
      count=$((count+1))
    fi
    count=$((count+1))
  done
fi