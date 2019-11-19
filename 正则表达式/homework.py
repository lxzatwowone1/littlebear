"""
作业，从标准输入输入一个端口名称，返回该端口运行情况描述中的address值(address is /Internet address is)
"""
import os
import re
def read_file(port):
    f = open("/home/tarena/exc.txt")
    while True:
        data = ''
        for line in f:                #遍历文件是没一行
            if line == "\n":
                break
            data += line
        if not data:
            return "no"
        obj = re.match(r'\S+',data)
        if port == obj.group():
            p = r'([0-9a-f]{4}\.){2}[0-9a-f]{4}'
            obj = re.search(p,data)

            if obj:
                return obj.group()

port = input("请输入端口号：")
a = read_file(port)
print(a)


