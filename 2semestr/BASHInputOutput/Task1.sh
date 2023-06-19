#!/bin/bash
#Перенаправьте ввод так чтобы выполнить команды хранящиеся в файле FileForTask1
#если возникнут ошибки перенаправьте в файл errors
#в конце очистите файл не удаляя его

exec 0< FileForTask1.txt
exec 2> Errors
exec 1>answer
while read line
do
    $line
done

cat /dev/null > FileForTask1


