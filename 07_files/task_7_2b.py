#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

cfg_lines = []

with open('config_sw1.txt', 'r') as f:
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
file = open('config_sw1_cleared.txt', 'w')
file.writelines(cfg_lines2)
file.close()



