#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def parse_cdp_neighbors(command_output):
   temp_dict = {}
   temp_tuple1 = ()
   temp_tuple2 = ()
   temp_list = []
   temp_list1 = []
   temp_list2 = []
   output = []
   output = command_output.split('\n') 
   for string in output:
       if string.find('>show cdp neighbors') > 0:
           name = string[0:string.find('>show cdp neighbors')]
       else:
           if string.startswith('R'):
               temp_tuple1 = ()
               temp_tuple2 = ()
               temp_list1 = []
               temp_list2 = []             
               temp_list1.insert(0,name)
               temp_list1.insert(1,string[13:20].replace(' ',''))
               temp_list2.insert(1,string[0:2])
               temp_list2.insert(2,string[-7:].replace(' ',''))
               temp_tuple1 = tuple(temp_list1)
               temp_tuple2 = tuple(temp_list2)
               temp_dict.update({temp_tuple1:temp_tuple2}) 
           else:
               pass
   return(temp_dict)








if __name__ == "__main__":
    f = open('sh_cdp_n_sw1.txt')
    string = f.read()
    print(parse_cdp_neighbors(string))
   
