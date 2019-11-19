"""
block_io.py
socket 套接字非阻塞示例
"""
from socket import *
from time import sleep
ADDR = ("0.0.0.0",5566)

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(3)

sockfd.setblocking(False)
sockfd.settimeout(5)
print("Listen to")

#设置套接字
while True:
    try:
        connfd,addr = sockfd.accept()
        print("connect from",addr)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)



sockfd.setblocking()

rs, ws, xs=select(rlist, wlist, xlist[, timeout])