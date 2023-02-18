#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:20:23 2023

@author: stu

数据分析师大黄近期升职了，月薪27000元，公司决定根据他的绩效分数发放年终奖金。
大黄的绩效分数为9分，年终绩效打分范围为0-10。同时他也获得了全勤奖，只有部分员工获得全勤奖，大部分员工没有全勤奖。

公司按以下规则给予相应奖励:
绩效为1-3分，不发放年终奖金，只发放价值（绩效分数*50元）的春节礼品

绩效为4-6分，给予2个月工资作为年终奖金，并发放价值（绩效分数*80元）的春节礼品; 
    如果绩效5分或6分，全勤奖员工明年将获得额外2天带薪假期
绩效为7-8分，给予4个月工资作为年终奖金，并发放价值（绩效分数*120元）的春节礼品; 
    全勤奖员工明年将获得额外5天带薪假期
绩效为9-10分，给予半年工资作为年终奖金，并发放价值（绩效分数* 150元）的春节礼品; 
    全勤奖员工明年将获得额外8天带薪假期

因奖励规则较为复杂，大黄想为同事写一个小程序搞懂自己和大家的所有年终奖励，请你帮忙~

"""

def Bonus(performance:int, full_time_award:bool):
    if 3 >= performance and performance>= 1:
        print(f"您的奖励：{performance * 50}元的春节礼品")
    elif 6 >= performance and performance>= 4:
        print(f"您的奖励：{performance * 80}元的春节礼品")
        if full_time_award:
            print("您还获得额外2天带薪假期")
    elif 8 >= performance and performance>= 7:
        print(f"您的奖励：{performance * 120}元的春节礼品")
        if full_time_award:
            print("您还获得额外5天带薪假期")
    elif 10 >= performance and performance>= 9:
        print(f"您的奖励：{performance * 150}元的春节礼品")
        if full_time_award:
            print("您还获得额外8天带薪假期")
    return None

performance = 9
fullTimeAward = True

Bonus(performance,fullTimeAward)
