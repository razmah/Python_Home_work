""" Требуется вычислить, сколько раз встречается 
некоторое число k в массиве list_1 
Найдите количество и выведите его """

import os

os.system("cls")

list1 = [int(i) for i in input("Введите список чисел: ").split()]

print(list1.count(int(input("Введите число: "))))


