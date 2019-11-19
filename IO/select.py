from socket import *
from select import select
from time import sleep

#创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",5566))
s.listen(19910711)
print("waitting for connect。。。")
rlist,wlist,xlist = [s],[],[]
# print(rlist)
# print(wlist)
# print(xlist)
# 监控IO对应事件的发生
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    #遍历返回值列表，根据情况讨论
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)
        else:
            #某个客户端套接字就绪（某个客户端给我发了消息）
            print("获取消息来自",r.getpeername())
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            # r.send("收到了消息么么嗒\n".encode())
            wlist.append(r)

    for w in ws:
        w.send(b"ok\n")
        wlist.remove(w)






