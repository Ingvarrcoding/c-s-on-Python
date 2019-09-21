# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

import sys

with open('test_file.txt', 'w', encoding='utf-8') as test_file:
    test_file.write('сетевое программирование\n')
    test_file.write('сокет\n')
    test_file.write('декоратор\n')
with open('test_file.txt', encoding='utf-8') as test_file:
    for each_line in test_file:
        print(each_line, end="")