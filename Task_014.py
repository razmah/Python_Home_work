''' Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа n '''

import os

os.system('cls')

n = int(input('Введите целое число: '))
m = 1

print('\nЦелые степени двойки: ', end = '')

while m < n:
    if m < n:
        if m * 2 > n:
            break
        else:
            m = m * 2
            print(m, end = ' ')
print('\n')
