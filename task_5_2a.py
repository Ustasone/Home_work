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
dec_mask=int(mask)
last = 32-dec_mask
octets = numbers.split(".")
bit_address = '{:08b}{:08b}{:08b}{:08b}'.format(int(octets[0]), int(octets[1]), int(octets[2]), int(octets[3]))



#print(bit_address)

net_addr = bit_address[0:dec_mask]
print('bit_addt', net_addr)
full_net_addr = net_addr+'0'*last
print('new_full_addr', full_net_addr)

ip_template = '''
Network:
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}
'''


print(ip_template.format( int(full_net_addr[0:8], 2), int(full_net_addr[8:16], 2), int(full_net_addr[16:24], 2), int(full_net_addr[24:32], 2), int(full_net_addr[0:8], 2), int(full_net_addr[8:16], 2), int(full_net_addr[16:24], 2), int(full_net_addr[24:32], 2)))

netmask_template = '''
Netmask:
{}
{:8} {:8} {:8} {:8}
{:<8} {:<8} {:<8} {:<8}
'''
bitmask = "1"*dec_mask
bitlast = "0"*last
#print(bitmask) 
#print(bitlast)
fullbitmask = bitmask+bitlast
#print(fullbitmask)

print( netmask_template.format(dec_mask, fullbitmask[0:8], fullbitmask[8:16], fullbitmask[16:24], fullbitmask[24:32], int(fullbitmask[0:8], 2), int(fullbitmask[8:16], 2), int(fullbitmask[16:24], 2), int(fullbitmask[24:32], 2)))
