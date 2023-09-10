""" Настольная игра Скрабл(Scrabble), где 
каждая буква имеет свою ценность. 
Напишите программу, которая вычисляет стоимость пользователем
слова k и выводит его. Будем считать, что на вход подается только
одно слово, которая содержит либо английские, либо только
русские буквы. """

import os
# import re

os.system("cls")

# Вариант решения 1:

# def isCyrillica(text):
#     return bool(re.search('[а-яА-Я]', text))

# text = input("Введите слово на русском или английском языке: ").upper()

# enList = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP',
# 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}

# ruList = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ',
# 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}

# if isCyrillica(text):
#     print(sum([key for i in text for key, value in ruList.items() if i in value]))
# else:
#     print(sum([key for i in text for key, value in enList.items() if i in value]))

# Вариант решения 2:

text = input("Введите слово на русском или английском языке: ").upper()

en = "qwertyuiopasdfghjklzxcvbnm".upper()
ru = "ёйцукенгшщзхъфывапролджэячсмитьбю".upper()

enList = {
    1: "AEIOULNSTR", 
    2: "DG", 
    3: "BCMP", 
    4: "FHVWY", 
    5: "K", 
    8: "JX", 
    10: "QZ"}

ruList = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ",
}

if text[0] in ru:
    sum = 0
    for i in text:
        for key, value in ruList.items():
            if i in value:
                sum += key 
    print(sum)

else:
    if text[0] in en:
        sum = 0
        for i in text:
            for key, value in enList.items():
                if i in value:
                    sum += key
    print(sum)
