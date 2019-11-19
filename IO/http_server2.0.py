"""
http_server.py
功能: 1. 获取来自浏览器的请求（request）
     2. 如果请求内容为'/'那么将 index.html给浏览器
     3. 如果不是'/' 返回给客户端404
"""
from socket import *
from select import *

# 服务器地址
ADDR = ('127.0.0.1', 8888)

class HTTPServer:

    def __init__(self,host="127.0.0.1",port=8000,dir=None):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.dir = dir
        self.create_socket()

    def create_socket(self):
        self.s = socket()
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.s.bind(self.address)

    def server_forever(self):
        self.s.listen(5)
        print("Listen the port %d"%self.port)
        p = epoll()
        p.register(s,)

        while True:
            events = p.poll()  # 阻塞等待IO发生
            print(events)  # [(fileno,event)]
            for fd, event in events:
                # if结构区分哪个IO就绪 fd->fileno  event->IO类别
                if fd == s.fileno():
                    c, addr = fdmap[fd].accept()
                    print("Connect from", addr)
                    p.register(c, EPOLLIN | EPOLLERR)  # 关注客户端套接字
                    fdmap[c.fileno()] = c  # 将其添加到查找字典
                # 通过按位与判断是否为POLLIN就绪
                elif event & POLLIN:
                    data = fdmap[fd].recv(1024).decode()
                    if not data:
                        p.unregister(fd)  # 取消关注
                        fdmap[fd].close()
                        del fdmap[fd]  # 从字典中移除
                        continue
                    print(data)
                    fdmap[fd].send(b'OK\n')

#  处理http请求
def request(connfd):
    # 获取http请求
    data = connfd.recv(1024 * 4).decode()
    if not data:
        return
    # 简单的解析
    request_line = data.split('\n')[0]
    info = request_line.split(' ')[1]  # 提取请求内容
    print("请求内容:",info)
    if info == '/':
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        with open('index.html') as f:
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "Sorry...."
    # 将响应发送给浏览器
    connfd.send(response.encode())


# 搭建tcp网络，启动整个代码
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(3)
    while True:
        connfd, addr = sockfd.accept()
        request(connfd)


if __name__ == '__main__':
    """
    通过HTTPServer类可以快捷的搭建一个服务器，帮助我展示我的网页
    使用原则：1.能够为使用者实现的尽量都实现
            2.不能替用户决定的数据量让用户传入类中
            3.不能替用户决定的功能让用户重写
    
    """
    main()
host = "0.0.0.0"
port = 8000
dir ="./static"

httpd = HTTPServer(host,port,dir)  #实列化变量
httpd.server_forever() #启动
