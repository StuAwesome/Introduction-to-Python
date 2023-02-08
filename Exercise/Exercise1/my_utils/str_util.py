#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:15:01 2023

1. string_util.py
    str_reverse(s)反转字符串
    substr(s,x,y)按照下标切片
    
@author: stu
"""

print('导入了str_util.py')

def str_reverse(s):
    '''
    Parameters
    ----------
    s : string
        将被反转的字符串

    Returns
    -------
    string
        反转后的字符串

    '''
    return s[::-1]

def substr(s,x,y):
    '''
    

    Parameters
    ----------
    s : string
        被切片的字符串.
    x : int
        开始切片index
    y : int
        切片的结束下标.

    Returns
    -------
    string
        完成后的字符串.

    '''
    return s[x:y]


# 测试

if __name__ =="__main__":
    print(str_reverse("12345"))
    print(substr("12345", 1, 3))