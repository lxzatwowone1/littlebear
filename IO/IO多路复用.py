from select import  select
from socket import *
from time import sleep

s = socket()
s.bind(("0.0.0.0",5566))
s.listen(3)

f = open("demo.py","r")
sleep(5)

print("监控IO")
rs,ws,xs = select([s,f],[f],[],3)
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)