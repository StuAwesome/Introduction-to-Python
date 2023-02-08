#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:08:37 2023

@author: stu

创建my_utils包 and 两个模块
1. string_util.py
    str_reverse(s)反转字符串
    substr(s,x,y)按照下标切片
2. file_util.py
    print_file_info(file_name) 接受传入文件的路径
    append_to_file(file_name,data)

"""

import my_utils.str_util
import my_utils.file_util
# 两个print都执行成功
print(my_utils.str_util.str_reverse("黑马程序员"))
