#!/bin/bash
#выведите отдельные слова из файла filefortask2.txt в столбик
IFS=";"
for var in $(cat filefortask2.txt)
do
  echo " $var"
done

