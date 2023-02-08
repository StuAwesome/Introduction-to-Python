#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("file_util导入成功")

def print_file_info(file_name):
    '''
    功能是给定文件内容输出到控制台中

    Parameters
    ----------
    file_name : 读取的文件路径
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    f = None
    # None 表示 False，有内容就是True
    try:
        f = open(file_name,'r',encoding=("UTF-8"))
        print(f.read())
    except Exception as e:
        print(f"文件出现异常了：{e}")
    finally:
        if f:
            f.close()
            
def append_to_file(file_name,data):
    '''
    将数据追加到指定文件中

    Parameters
    ----------
    file_name : file
        指定的文件中.
    data : TYPE
        指定的数据.

    Returns
    -------
    None.

    '''
    f = open(file_name,'a',encoding=("UTF-8"))
    f.write(data)
    f.write("/n")
    f.close()
    
    
# test
if __name__ == "__main__":
    append_to_file("/Users/stu/Desktop/Introduction-to-Python-main/Exercise/Exercise1/test_append.txt","黑马程序员" )
    
    