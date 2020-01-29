#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

with open('config_sw1.txt', 'r') as f:
    for string in f:
            for i in ignore:
                if string.find(i) >= 0:
                    string = '!'
                    break
                else:
                    pass
            if string.startswith('!'):
                pass
            else:
                print(string.rstrip('\n')) 


            
