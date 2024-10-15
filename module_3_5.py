#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_multiplied_digits(number):
    str_number = str(number) # извлекаем строковое представление числа
    first = int(str_number[0]) # первый символ в числовом представлении
    if len(str_number) >1 :
 # умножаем 1 число на результат работы функции (второе число)
        return first * get_multiplied_digits(int(str_number[1:]))
    else: # строка закончилась
        return int(str_number)

result = get_multiplied_digits(40203)
print(result)



