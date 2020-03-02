#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

def create_network_map(filenames):
    for file in filenames:
        f = open(file) 
        string = f.read()
        output = []
        output = string.split('\n')
        for command in output:
            if string.find('>show cdp neighbors') > 0:
                name = string[0:string.find('>show cdp neighbors')]
                if name.find('SW') > 0
       else:


def parse_cdp_neighbors(command_output)
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
           if name.startswith('R'):
               if string.startswith('R') or startswith('SW'):
                   temp_tuple1 = ()
                   temp_tuple2 = ()
                   temp_list1 = []
                   temp_list2 = []             
                   temp_list1.insert(0,name)
                   temp_list1.insert(1,string[17:24].replace(' ',''))
                   temp_list2.insert(1,string[0:3].replace(' ',''))
                   temp_list2.insert(2,string[-7:].replace(' ',''))
                   temp_tuple1 = tuple(temp_list1)
                   temp_tuple2 = tuple(temp_list2)
                   temp_dict.update({temp_tuple1:temp_tuple2}) 
               else:
                   pass
           else:
               if name.startswith('SW'):
                   if string.startswith('R') or startswith('SW'):
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



files = [ 'sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt' ]
create_network_map(filenames)
