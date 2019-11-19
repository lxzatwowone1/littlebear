# 1.匹配邮箱地址
# 2.匹配数字 12 -133 -1.6 -4.6 45.8% 1/2）
# 3.匹配一段文字中文书名
# 《啊-大海》 《哈木列特》
# 4.匹配身份证号 620104199107110830


import re
a = "《哈木,雷霆》,《流浪地球》,《最后一个地球人》"
b = re.findall(r"《.+?》",a)
print(b)

c = "gjboy2007@qq.com"
pattern = r"\w+@\w+(\.com)?(\.cn)?"
d = re.search(pattern,c).group()
print(d)

f = re.findall(r'\d{17}(\d|X)',"11008119990126103X")
print(f)