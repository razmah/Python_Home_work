''' Задача 22. 
Даны два неупорядоченных набора целых чисел (может быть
с повторениями). Выдать без повторений в порядке возрастания
те числа, которые встрчаются в обоих наборах. 
Пользователь вводит 2 числа. n - количество первого множества,
m - количество второго множества. Затем пользователь вводит
сами элементы множеств. '''

import os
import random

os.system("cls")

n = int(input("Введите количество n элементов: "))
numListN = [random.randint(1, 100) for i in range(n)]
print(numListN)

m = int(input("Введите количество m элементов: "))
numListM = [random.randint(1, 100) for i in range(m)]
print(numListM)

mnoz1 = set(numListM) # Срезаем повторяющиеся числа
mnoz2 = set(numListN) # --//--//--

sumMnoz = sorted(mnoz1.intersection(mnoz2))
print(*sumMnoz)