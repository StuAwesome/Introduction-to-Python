#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:11:06 2023

@author: stu
"""
'''
1. 【作文题】 1.不运行代码，直接判断以下运行结果是否会出现错误警告，并预测函数最终返回结果的数据类型：
①def func(c, d): ''' c: int d: int ''' return c / d 
# 报错
​②def func(c, d): ''' c: float d: float ''' return c >= d or c <= d
# 不报错
③def func(c, d): ''' c: float d: float ''' print("the return value is: ") c * d - 666
# 不报错
2.不运行代码，直接判断以下函数调用后的运行结果是否会出现错误警告，并预测函数最终返回结果的数据类型 ：
①sentence = "我不做人了， JoJo!" def func(): print(sentence) 
②sentence = "我不做人了，JoJo!" def func(): sentence = sentence + "欧拉欧拉欧拉欧拉" print(sentence) return sentence 
③sentence = "我不做人了，JoJo!" def func(): sentence = "欧拉欧拉欧拉欧拉" global sentence print(sentence) return sentence 
④sentence = "我不做人了，JoJo!" def func(): global sentence sentence = "欧拉欧拉欧拉欧拉" print(sentence) return sentence
'''
# 3.请把以下lambda函数改写成普通函数，并给转换后的函数写下docstring说明函数的作用和参数（如果看不懂，可以运行lambda代码观察结果）
# lambda z, g = 3: z**g
def Three_times_squared(z):
    '''
    
    '''
    return z ** 3

lambda a: True if a % 2 else False

def If_even(a):
    return not bool(a % 2)

If_even(4)


2. 【作文题】 大挑战：创造一个可以找出两数中最大公约数的函数

最大公约数是两个正整数都可以整除的最大整数
比如：25和10的最大公约数是5
def gcd(pn1, pn2): 
'''返回两个正整数的最大公约数 pn1 -- 正整数 pn2 -- 正整数 '''

程序应满足以下情况：
result = gcd(2,5)result的值为1
result = gcd(20,4)result的值为4
result = gcd(78,90)result的值为6

请写两个函数，一个使用循环语句，另一个使用递归原理

# 使用循环的函数
def gcd_iter(pn1, pn2): 
    '''使用循环语句返回两个正整数的最大公约数 pn1 -- 正整数 pn2 -- 正整数 '''
    small = min(pn1, pn2) 
    while small > 0: 
        if pn1 % small == 0 and pn2 % small == 0: 
            return small 
        else: small = small -1
# 使用递归的函数
def gcd_recur(pn1, pn2): '''使用递归语句返回两个正整数的最大公约数 pn1 -- 正整数 pn2 -- 正整数 ''' if pn2 == 0: return pn1 else: return gcd_recur(pn2, pn1 % pn2)
    
def gcd_iter(pn1, pn2): 
    # 循环
    '''
    使用循环语句返回两个正整数的最大公约数 
    pn1 -- 正整数 
    pn2 -- 正整数 
    '''
    small = min(pn1, pn2)
    while small > 0:
        if pn1 % small == 0 and pn2 % small == 0:
            return small
        else:
            small = small - 1
            
gcd_iter(18,5)
        

def gcd_recur(pn1, pn2):
    # 算法
    if pn2 == 0: 
        return pn1 
    else: 
        return gcd_recur(pn2, pn1 % pn2)
    
    
    
    
    
    