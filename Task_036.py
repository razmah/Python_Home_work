""" Задача 36. Напишите функцию 
print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую
по номеру строки и столбца. Аргументы num_rows и num_columns
указывают число строк и столбцов, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы. """

import os

os.system("cls")


def print_operation_table(operation, num_rows=6, num_columns=6):
    
    for i in range(1, num_rows + 1):
        list1 = list()
        for j in range(1, num_columns + 1):
            result = operation(i, j)
            list1.append(result)

        print(*list1)

print_operation_table(lambda x, y: x * y)
