#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
broadcast = "255.255.255.255"
zero = "0.0.0.0"
ipaddress = input('Enter ip-address:')

#for octet int ipaddress:



ipadd = ipaddress.split('.')


if int(ipadd[0])  >= 1 and int(ipadd[0]) <= 223: 
   print('unicast') 
elif int(ipadd[0]) >= 224 and int(ipadd[0]) <= 239:
   print('multicast')
elif broadcast == ipaddress:
    print('local broacast')
elif zero == ipaddress:
    print('unassigned')
else:
    print('unused')
