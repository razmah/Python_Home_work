'''Задача 10: На столе лежат n монеток. Некоторые из них лежат 
решкой, а некоторые гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были 
вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть. '''

import os
import random

os.system("cls")

n = int(input('Введите количество монет: '))

random_coins = [random.randint(0, 1) for i in range(n)]
print(f'Список монет: {random_coins}')
print(f'Количество монет решкой: {random_coins.count(0)} \nКоличество монет гербом: {random_coins.count(1)}') 

if random_coins.count(0) > random_coins.count(1):
    temp = random_coins.count(1)
else:
    temp = random_coins.count(0)

print(f'Минимальное количество монет, которые нужно перевернуть: {temp}')

