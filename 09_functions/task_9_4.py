#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
'''
    for item in ignore:
        if command.find(item) >= 0:
            #print('finded') 
            #print(command)
            result = 'True'
            break
        else:
            result = 'False'
    return(result)


def convert_config_to_dict(config_filename):
    command_dict = {}
    subcommand = []
    with open(config_filename, 'r') as f:
        for string in f:
            if string.startswith('!'):
                pass
            else:
                if ignore_command(string, ignore) == 'True':
                    pass
                else:
                    if string.startswith(' '):
                        subcommand.append(string)
                        command_dict[temp] = [item for item in string] 
                    else:
                        temp = string
                        command_dict.update({string: ''})
        return(command_dict)
'''
            else:
                if string.startswith(' '):
                    if ignore_command(string, ignore) == 'False':
                        #print(ignore_command(string, ignore))
                        subcommand.append(string)
                        #print('=======subcommand=======')
                        #print(subcommand)
                        command_dict.setdefault(temp, subcommand)
                        #print(command_dict)
                    else:
                        pass
                else:
                    #subcommand = []
                    temp = string
                    command_dict.update({string: ''})

    return(command_dict)
'''
print(convert_config_to_dict('config_sw1.txt'))
