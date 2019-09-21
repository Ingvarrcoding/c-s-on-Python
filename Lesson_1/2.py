# 2. Каждое из слов «class», «function», «method» записать в байтовом типе
# без преобразования в последовательность кодов (не используя методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

str_1 = b'class'
str_2 = b'function'
str_3 = b'method'
print(type(str_1))
print(str_1)
print(len(str_1))
print(type(str_2))
print(str_2)
print(len(str_2))
print(type(str_3))
print(str_3)
print(len(str_3))

'''
<class 'bytes'>
b'class'
5
<class 'bytes'>
b'function'
8
<class 'bytes'>
b'method'
6
'''