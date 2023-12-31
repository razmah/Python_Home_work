""" Задача 24. В фермерском хозяйстве в Карелии выращивают
чернику. Она растет на круглой грядке, причем кусты высажены
только по окружности. Таким образом, у каждого куста есть
ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени 
сбора на них выросто различное число ягод - га i-ом кусте
выросло ai ягодю.
В этом фермерском хозяйстве внедрена система автоматического 
сбора черники. Эта система состоит из управляющего модуля 
и нескольких собирающих модулей. Собирающий модуль за один заход,
находясь непосредственно перед некоторым кустом, собирает ягоды
с этого куста и с двух соседних с ним. 
Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки. """

import os

os.system("cls")

kustChernika = int(input("Введите количество кустов черники: "))
x = []
for i in range(kustChernika):
    numsChernika = int(input("Введите количество ягод на кусте: "))
    x.append(numsChernika)

xCount = []
for i in range(len(x)):
    xCount.append(x[i] + x[i - 1] + x[i - 2])

print(f"Максимальное количество черники с трёх кустов: {max(xCount)}")