num = int(input())

first = num // 100
second = num // 10 % 10
third = num % 10

print(first + second + third)
