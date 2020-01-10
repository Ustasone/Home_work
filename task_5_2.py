#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
network = input('Enter ip-address in style: 10.1.1.0/24 ',)
temp = network.split("/")
numbers = temp[0]
mask = temp[-1]
octets = numbers.split(".")
ip_template = '''
Network:
{:8} {:8} {:8} {:8}
{:08b} {:08b} {:08b} {:08b}
'''
print(ip_template.format(octets[0], octets[1], octets[2], octets[3], int(octets[0]), int(octets[1]), int(octets[2]), int(octets[3])))

