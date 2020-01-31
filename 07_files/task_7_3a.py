#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ignore = ['sw1', 'Mac', '---', 'Vlan']
new_dict = {}
j = 0
#print(new_dict) 
with open('CAM_table.txt', 'r') as f:
    for string in f:
        #j = j + 1
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
            string = (string.replace('  DYNAMIC   ',''))
            new_list = string.split()
            if len(new_list) > 0:
                new_dict.update({j: new_list})
                j = j + 1
print(new_dict)
P = 0
k = 0
n = 0
temp = {}
for k in range(j-1):
    for n in range(j-k-1):
        if new_dict[k][0] <= new_dict[k + 1][0]:
            pass
            #print('OK') 
            #P = 1
        else:
            temp.update({k: new_dict[k]})
            new_dict.update({k: new_dict[k + 1]})
            new_dict.update({k + 1: temp[k]})
            print(temp)
            P = 1  
            #print('NOK')    
    if P == 0:
        break
    else:
        pass

print(new_dict)
