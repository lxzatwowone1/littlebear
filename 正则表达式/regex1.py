"""
match对象生成者

"""


import re
s = "今年是2019年，建国70周年"
pattern = r'\d+'
#返回匹配结果的迭代对象
it = re.finditer(pattern,s)
#每次迭代到的是match对象（为了获取匹配内容更丰富的信息）
print(it)
for i in it:
    print(i.group()) #获取match对象对应的匹配内容


#完全匹配一个字符串
m = re.fullmatch(r'.+',s)
print(m.group())

n =re.match(r'\w+',s)
print(n.group())

q =re.search(r'\d',s)
print(q.group())