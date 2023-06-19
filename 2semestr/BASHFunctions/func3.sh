#!/bin/bash
function students() {
  echo "Введите количество учеников: "
  read number
  for ((a = 1; a <= number; a++))
    do
    echo "Введите балл за финальный тест: "
    read rate
    if [ $rate -ge 50 ]; then
      echo "True"
    else
      echo "Вы отчислены"
    fi
  done
}

students
