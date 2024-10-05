#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Функция print_params(a = 1, b = 'строка', c = True),
# принимает три параметра со значениями по умолчанию

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('Вывод значений параметров')
print_params()  # Вывод значений параметров
print()
print('Вызов print_params с разными аргументами.')

print_params(8, 'текст', False)
print_params(7, 'None')
print_params(a='один', b='False', c='три')
print_params(a='один', c='7')
print_params(c='6')
print_params()

print()
print('Проверяю работу вызовов print_params(b = 25) и print_params(c = [1,2,'
      '3])')

print_params(b=25)
print_params(c=[1, 2, 3])

print()

#Создаю список values_list с тремя элементами разных типов.')
values_list = [15, 'текст', True]

# Создаю словарь values_dict с ключами, соответствующими параметрам print_params
values_dict = {'a': True, 'b': 'столбец', 'c': 0}

print('Передаю values_list и values_dict в функцию используя распаковку')
print_params(*values_list)
print_params(**values_dict)

print()
print('Распаковка + отдельные параметры')

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)