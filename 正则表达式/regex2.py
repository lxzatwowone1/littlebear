"""
match对象演示

"""

import re
pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
m = regex.search('abcdefgh')
#属性变量
print(m.pos)
print(m.endpos)
print(m.re)
print(m.string)
print(m.lastgroup)
print(m.lastindex)

#属性方法
print(m.span())
print(m.start())
print(m.end())
print(m.groupdict())
print(m.groups())   #子组？？？
print(m.group())