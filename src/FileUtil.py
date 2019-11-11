#! /use/bin/python
# coding = utf-8
import os
import shutil


# 创建目录
def mkdir(path: str):
    # 去除首尾空格
    path = path.strip()
    # 去除尾部的 \ 符号
    path.rstrip('\\')
    # 判断路劲是否存在
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)


# 写文件
def write(fileName: str, context, model):
    # 去除字符串首尾的空格
    fileName = fileName.strip()
    #  读取目录名
    path = os.path.dirname(fileName)
    # 如果目录不存在则创建目录
    mkdir(path)
    # 读取文件名称
    name = os.path.basename(fileName)
    fp = open(fileName, model)
    fp.write(context + '\n')
    fp.close()
    return name


# 删除文件
def delFile(fileName: str):
    # 去除字符串首尾的空格
    fileName = fileName.strip()
    if os.path.exists(fileName):
        os.remove(fileName)


# 删除目录
def delDir(path: str, model):
    # 去除字符串首尾的空格
    path = path.strip()
    # 判断目录是否存在
    isExists = os.path.exists(path)
    if isExists:
        if model == 'rf':
            # 强制删除目录以及目录下所有文件
            shutil.rmtree(path)
        else:
            # 只有空目录才可以删除
            os.removedirs(path)