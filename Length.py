# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a sample script file.
"""
#calculating the length of a string through an iterative and a recursive method

def iter_len(string:str):
    epsilon = ''
    L=0
    if string==epsilon:
        return L
    else:
        while string!=epsilon:
            L+=1
            string=string[1:]
        return L
    

def rec_len(string:str):
    if string=='':
        return 0
    else:
        string=string[1:]
    return 1+rec_len(string)
    
