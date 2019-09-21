# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

str_1 = 'разработка'
str_2 = 'администрирование'
str_3 = 'protocol'
str_4 = 'standard'
print(f'Исходные строки:\n{str_1}, {str_2}, {str_3}, {str_4}\n')
str_1_byte = str_1.encode('utf-8')
str_2_byte = str_2.encode('utf-8')
str_3_byte = str_3.encode('utf-8')
str_4_byte = str_4.encode('utf-8')
print(f'Перевода из строчного представления в байтовое:\n{str_1_byte}\n{str_2_byte}\n{str_3_byte}\n{str_4_byte}\n')
str_1_str = str_1_byte.decode('utf-8')
str_2_str = str_2_byte.decode('utf-8')
str_3_str = str_3_byte.decode('utf-8')
str_4_str = str_4_byte.decode('utf-8')
print(f'Обратный перевод из байтового представления в строчное:\n{str_1_str}, {str_2_str}, {str_3_str}, {str_4_str}')

'''
Исходные строки:
разработка, администрирование, protocol, standard

Перевода из строчного представления в байтовое:
b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'
b'protocol'
b'standard'

Обратный перевод из байтового представления в строчное:
разработка, администрирование, protocol, standard
'''