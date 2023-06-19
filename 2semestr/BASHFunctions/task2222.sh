#!/bin/bash

formula() {
  weight=$1
  height=$2
  index=$(echo "$weight / ($height * $height)" | bc)
  echo $index
}

count() {
  index=$1
  if (($(echo "$index < 18.5" | bc -l))); then
    echo "Недостаточный вес"
  elif (($(echo "$index >= 18.5 && $index <= 25" | bc -l))); then
    echo "ИМТ в норме"
  else
    echo "Избыточный вес"
  fi
}

weight=$1
height=$2

index=$(formula $weight $height)
count $index
