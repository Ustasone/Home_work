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
a = 0

while a == 0:
    ipaddress = input('Enter ip-address:')
    mark = 1
    err = 0

    ipadd = ipaddress.split('.')

    count = len(ipadd)

    if count == 4:
        for octet in ipadd:
            if octet.isdigit():
                if int(octet) >= 0 and int(octet) <= 255:
                    digit = 1
                else:
                    mark = 0
                    digit = 1
            else:
                digit = 0
                mark = 0
                break
    else:
         err = 1

    if count == 4 and digit == 1 and mark == 1 and err == 0:
        a = 1
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
    else:
        a = 0
        print('WRONG IP')
