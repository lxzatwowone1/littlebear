"""
regex.py re模块示例

"""
import re
#目标字符串
s = "Alex:1994,Sunny:1996,Liu:1991"
pattern = r"(\w+):(\d+)"

#re模块调用
r = re.findall(pattern,s,flags=0)
print(r)

#compile对象调用
regex = re.compile(pattern)
l = regex.findall(s,0,11)
print(l)

#使用正则表达式切割字符串
i = re.split(r':|,',s)
print(i)

#替换正则匹配内容
s = re.sub(r'[^\w]','**',s)
print(s)