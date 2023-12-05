#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант - 11

def func():
    def inner(k):
        return k + 3
    return inner


if __name__ == '__main__':
    cnt = func()
    print(cnt(int(input())))
    print(cnt(int(input())))
