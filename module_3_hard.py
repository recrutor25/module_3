#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_structure_sum(*data_structure):
    summa = 0
    for i in data_structure:
        if isinstance(i, list):
            for unit in i:
                summa += calculate_structure_sum(unit)

        elif isinstance(i, dict):
            for key, value in i.items():
                summa += calculate_structure_sum(key, value)

        elif isinstance(i, tuple):
            for unit in i:
                summa += calculate_structure_sum(unit)

        elif isinstance(i, set):
            for unit in i:
                summa += calculate_structure_sum(unit)

        elif isinstance(i, str):
            summa += len(i)

        elif isinstance(i, int):
            summa += i
 
    return summa


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
print(data_structure)