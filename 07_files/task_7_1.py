#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

template = '''
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
'''


with open('ospf.txt', 'r') as f:
    for new_ospf in f:
        new_ospf = new_ospf.replace(',','')
        new_ospf = new_ospf.replace('[','')
        new_ospf = new_ospf.replace(']','')
        new_ospf = new_ospf.replace('O','OSPF')
        #print(new_ospf)
        ospf = new_ospf.split()
        #print(ospf)
        print(template.format(ospf[0],ospf[1],ospf[2],ospf[3],ospf[4],ospf[5]))

        



