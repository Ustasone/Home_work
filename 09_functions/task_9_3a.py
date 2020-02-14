#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
                if string.startswith(' switchport mode access'):
                    vlan = 1
                    access_dict.update({intf: vlan})
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
print(get_int_vlan_map('config_sw2.txt'))

