#!/bin/bash
# напишите скрипт который принимает несколько ключей и несколько параметров
# если ключ -n то после него идет имя
# В параметрах передается "к сожалению" и "отчислен"
# и выводит надпись: студент Имя \n к сожалению отчислен
count=0

if [ $# -eq 0 ]
then
  echo "Введите параметры"
else
  for param in "$@"
  do
    if [ "$param" == "-n" ]
    then
      name="${@:((count+2)):1}"
      text1="${@:((count+3)):1}"
      text2="${@:((count+4)):1}"
      text3="${@:((count+5)):1}"
      count=$((count+1))
    fi
    count=$((count+1))
  done
  echo "Студент $name"
  echo "$text1 $text2 $text3"
fi
