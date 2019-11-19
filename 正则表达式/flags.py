"""
功能扩展标志
"""
import re

s = """Hello
北京欢迎你
"""
#常量就是数字
#只能匹配ASCII编码

# regex = re.compile(r'\w+',flags=re.A)
# regex = re.compile(r'[[A-z]+')
# regex = re.compile(r'[[a-z]+',flags=re.I)
# regex = re.compile(r'.+',flags=re.S)
regex =re.compile(r'^北京') 
l = regex.findall(s)
print(l)
