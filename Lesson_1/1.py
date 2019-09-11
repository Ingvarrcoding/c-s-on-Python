# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

str_1 = 'разработка'
str_2 = 'сокет'
str_3 = 'декоратор'
print(type(str_1))
print(type(str_2))
print(type(str_3))
print(str_1)
print(str_2)
print(str_3)

uni_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
uni_2 = '\u0441\u043e\u043a\u0435\u0442'
uni_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(type(uni_1))
print(type(uni_2))
print(type(uni_3))
print(uni_1)
print(uni_2)
print(uni_3)

'''
<class 'str'>
<class 'str'>
<class 'str'>
разработка
сокет
декоратор
<class 'str'>
<class 'str'>
<class 'str'>
разработка
сокет
декоратор
'''