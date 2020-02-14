#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_filename):
    tr_vl_list = []
    access_dict = {}
    trunk_dict = {}
    ports = (access_dict, trunk_dict)
    with open(config_filename, 'r') as f:
        for string in f:
            if string.startswith('interface'):
               intf = string[10:].strip()
            else:
                if string.startswith(' switchport access'):
                    vlan = int(string[24:].strip())
                    access_dict.update({intf: vlan})
                else:
                    if string.startswith(' switchport trunk allowed'):
                        temp_list = string[31:].strip().split(',')
                        result = [int(item) for item in temp_list]
                        trunk_dict.update({intf: result})
                    else:
                        pass
    return(ports)
print(get_int_vlan_map('config_sw1.txt'))
