#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:34:56 2023

@author: stu
question1
① # 不会死循环
number = 4 
while number > 1: 
    print(number) 
    number = number - 1 
    else: print(number)
    

② # 不会死循环
myLingshi = 10 
while True: 
    if myLingshi < 7: 
        print('一下子全部吃光啦') 
        break 
    print(myLingshi) 
    myLingshi = myLingshi - 1 
    if myLingshi != 8: 
        print(f"我的零食只有{myLingshi}个了") 
    else: continue print('零食全部吃光啦~')
③mymoney = 100 while not False: if mymoney <= 0: break else: for i in range(1): print(f"我只有{mymoney}块") else: print("我财务自由啦！")

"""

'''
2.请分别用for loop 和while loop 写一个程序
该程序用来判断变量text中是否有“你”字
如果有的话，请告知用户：这段文字中有"你"字，共出现了n次。 (n为阿拉伯数字，反映实际出现次数）
如果没有的话，请告知用户：本段文字并没有出现"你"字。
第一个程序只能使用for loop，第二个程序只能使用while loop
这个程序需在以下三个例子中都成功运行:
'''

text = input("输入text：")
n = 0
if "你" in text:
    for i in text:
        if i == "你":
            n += 1
    print(f"这段文字中有\"你\"字，共出现了{n}次")
else:
    print("本段文字并没有出现\"你\"字。")

text = input("输入text：")
n = 0
i = 0
if "你" in text:
    while i < len(text):
        if text[i] == "你":
            n += 1
    print(f"这段文字中有\"你\"字，共出现了{n}次")
else:
    print("本段文字并没有出现\"你\"字。")

'''
3. 挑战：创造三三乘法表
你朋友的小孩7岁了，朋友想教她学乘法表。先从1-3的乘法开始。
你能帮忙写一个程序罗列出1-3的乘法运算结果吗？请随意使用for loop或者while loop
'''


for i in range(1,4):
    j = 1
    while j <= 3:
        print(f"{i} * {j} = {i*j}",end = "; ")
        j += 1
    else:
        print("")


