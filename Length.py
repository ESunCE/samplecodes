# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a sample script file.
"""

def iter_len(string):
    epsilon = ''
    L=0
    if string==epsilon:
        return L
    else:
        while string!=epsilon:
            L+=1
            string=string[1:]
        return L
    

def rec_len(string):
    if string=='':
        return 0
    else:
        string=string[1:]
    return 1+rec_len(string)
    