#!/bin/bash
# напишите скрипт для регистрации если передан ключ -r запрашиваем логин и пароль.
# Заносим в файл и выводим "Вы успешно зарегестрировались"
# если не передан ключ выводим надпись "А что вы тогда тут делаете?"


if [  $1 = "-r"  ]; then
  echo "введите логин и пароль"
  read -p login password
  echo "$login - $password" >> fileforbase.txt
  echo "вы успешно зарегистрировались"
else
  echo "А что вы тогда тут делаете?"
fi


