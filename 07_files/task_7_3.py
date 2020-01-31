#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt.
Каждая строка, где есть MAC-адрес, должна быть обработана таким образом,
 чтобы на стандартный поток вывода была выведена таблица вида (показаны не все строки из файла):

 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ignore = ['sw1', 'Mac', '---', 'Vlan']

new_list = []
with open('CAM_table.txt', 'r') as f:
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
            string = string.rstrip('\r\n')
            string = string.rstrip('\n')
            string = string.replace('  DYNAMIC   ','')
            new_list = string.split()
            if len(new_list) > 0:
                print(string)
            #print(ignore)



