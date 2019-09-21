# 5.	Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
# результаты из байтовового в строковый тип на кириллице.

import subprocess
import chardet

args = ['ping', 'yandex.ru']
ya_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in ya_ping.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

'''
{'encoding': 'ascii', 'confidence': 1.0}


{'encoding': 'IBM866', 'confidence': 0.9308723921959009}
Обмен пакетами с yandex.ru [5.255.255.80] с 32 байтами данных:

{'encoding': 'IBM866', 'confidence': 0.9637267119204622}
Ответ от 5.255.255.80: число байт=32 время=7мс TTL=54

{'encoding': 'IBM866', 'confidence': 0.9637267119204622}
Ответ от 5.255.255.80: число байт=32 время=7мс TTL=54

{'encoding': 'IBM866', 'confidence': 0.9637267119204622}
Ответ от 5.255.255.80: число байт=32 время=8мс TTL=54

{'encoding': 'IBM866', 'confidence': 0.9637267119204622}
Ответ от 5.255.255.80: число байт=32 время=9мс TTL=54

{'encoding': 'ascii', 'confidence': 1.0}


{'encoding': 'IBM866', 'confidence': 0.99}
Статистика Ping для 5.255.255.80:

{'encoding': 'IBM866', 'confidence': 0.9533417258006296}
    Пакетов: отправлено = 4, получено = 4, потеряно = 0

{'encoding': 'IBM866', 'confidence': 0.99}
    (0% потерь)

{'encoding': 'IBM866', 'confidence': 0.99}
Приблизительное время приема-передачи в мс:

{'encoding': 'IBM866', 'confidence': 0.9955163083206161}
    Минимальное = 7мсек, Максимальное = 9 мсек, Среднее = 7 мсек
'''

args = ['ping', 'youtube.com']
yt_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in yt_ping.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

'''
{'encoding': 'ascii', 'confidence': 1.0}


{'encoding': 'IBM866', 'confidence': 0.9308723921959009}
Обмен пакетами с youtube.com [64.233.162.190] с 32 байтами данных:

{'encoding': 'IBM866', 'confidence': 0.9637267119204622}
Ответ от 64.233.162.190: число байт=32 время=19мс TTL=46

{'encoding': 'IBM866', 'confidence': 0.9637267119204622}
Ответ от 64.233.162.190: число байт=32 время=19мс TTL=46

{'encoding': 'IBM866', 'confidence': 0.9637267119204622}
Ответ от 64.233.162.190: число байт=32 время=19мс TTL=46

{'encoding': 'IBM866', 'confidence': 0.9637267119204622}
Ответ от 64.233.162.190: число байт=32 время=19мс TTL=46

{'encoding': 'ascii', 'confidence': 1.0}


{'encoding': 'IBM866', 'confidence': 0.99}
Статистика Ping для 64.233.162.190:

{'encoding': 'IBM866', 'confidence': 0.9533417258006296}
    Пакетов: отправлено = 4, получено = 4, потеряно = 0

{'encoding': 'IBM866', 'confidence': 0.99}
    (0% потерь)

{'encoding': 'IBM866', 'confidence': 0.99}
Приблизительное время приема-передачи в мс:

{'encoding': 'IBM866', 'confidence': 0.9955163083206161}
    Минимальное = 19мсек, Максимальное = 19 мсек, Среднее = 19 мсек
'''