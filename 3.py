# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

str_1 = b'attribute'
str_2 = b'класс'
str_3 = b'функция'
str_4 = b'type'
print(str_1)
print(str_2)
print(str_3)
print(str_4)

'''
Для слов на кирилице появляется ошибка "SyntaxError: bytes can only contain ASCII literal characters."
В байтовом типе в коротком виде возможна запись только на латинице.
'''