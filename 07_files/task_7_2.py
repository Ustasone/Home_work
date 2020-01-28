#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

with open('config_sw1.txt', 'r') as f:
    for string in f:
        if string.startswith('!'):
            pass
            #print('find')
        else:
            #string =(string.rstrip('!\n'))
            #print(string)
            print(string.rstrip('!\n'))


