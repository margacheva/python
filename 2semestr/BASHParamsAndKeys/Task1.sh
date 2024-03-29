#!/bin/bash
# Напишите скрипт который дает студенту 3 секунды чтобы ответить на вопрос "ФИО преподавателя"
# Если он не успевает выводится "Вы отчислены"

echo "У вас есть 3 секунды, чтобы ответить на вопрос: ФИО преподавателя"
read -t 3 answer # Считываем ответ с таймаутом 3 секунды
#ключ t - время ожидания ввода в секундах

if [ -z "$answer" ]; then # Если ответ не был введён
#ключ "-z"используется для проверки на пустую строку
    echo "Вы отчислены"
else # Иначе выводим ответ
    echo "Ответ: $answer"
fi
