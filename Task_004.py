''' Определите, можно ли от шоколадки размером a * b
долек отломить c долек, если разрешается сделать один разлом по 
прямой между дольками(то есть разломить шоколадку на 2 прямоугольника).
Выведите yes или no соответственно '''

a = int(input())
b = int(input())
c = int(input())

if (c % a == 0 or c % b == 0) and (c <= a * b):
    print('yes')
else:
    print('no')