#!/usr/bin/env python3
# -*- coding: utf-8 -*-
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string , list_to_search):
    count_calls()
    is_str = True
    for s in list_to_search:
        if string.upper() == s.upper():
            is_str = True
        else:
            is_str = False
    return is_str

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

