""" Требуется найти в массиве list1 самый близкий по
величине элeмент к заданному числу k и вывести его """

import os

os.system("cls")

list1 = [int(i) for i in input("Введите список чисел: ").split()]
k = int(input("Введите число для поиска: "))
list2 = []

for i in list1:
    list2.append(abs(k - i))
    print(list2)
num = list2.index(min(list2))
print(num)
print(f"Ближайшее число: {list1[num]}")