#!/usr/bin/env python3
from sys import argv
# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
file_read = argv[1]
file_write = argv[2]

ignore = ['duplex', 'alias', 'Current configuration']

cfg_lines = []

with open( file_read, 'r') as f:
    for string in f:
            for i in ignore:
                if string.find(i) >= 0:
                    string = '#'
                    break
                else:
                    pass
            if string.startswith('#'):
                pass
            else:
                string = string.rstrip('\n')
                cfg_lines.append(string)
#print(cfg_lines)
cfg_lines2 = []
for line in cfg_lines:
    cfg_lines2.append( line + '\n' )
file = open( file_write, 'w')
file.writelines(cfg_lines2)
file.close()



