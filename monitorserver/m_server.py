#!/usr/bin/evn python
#-*-coding:utf8-*-
'''
Created on 2018年2月1日

@author: root
'''

import socketserver

class myTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print "got connection from:%s",self.client_address
        while 1:
            self.data = self.request.recv(1024)
            print self.data
            self.request.sendall(self.data)

host,port = "",18000
server = socketserver.TCPServer((host,port),myTCPHandler)
server.serve_forever()




'''
from socket import *
from time import ctime
import threading
import re

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

def Deal(sock, user):
    while True:
        data = sock.recv(BUFSIZ)
        if data == 'quit':
            del clients[user]
            sock.send(data)
            sock.close()
            print '%s logout' %user
            break
        elif re.match('to:.+', data) is not None:
            data = data[3:]
            if clients.has_key(data):
                chatwith[sock] = clients[data]
                chatwith[clients[data]] = sock
            else:
                sock.send('the user %s is not exist' %data)
        else:
            if chatwith.has_key(sock):
                chatwith[sock].send("[%s] %s: %s" %(ctime(), user, data))
            else:
                sock.send('Please input the user who you want to chat with')


tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

clients = {}
chatwith = {}

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:',addr
    username = tcpCliSock.recv(BUFSIZ)
    print 'The username is:',username
    if clients.has_key(username):
        tcpCliSock.send("Reuse")
        tcpCliSock.close()
    else:
        tcpCliSock.send("Welcome!")
        clients[username] = tcpCliSock
        chat = threading.Thread(target = Deal, args = (tcpCliSock,username))
        chat.start()
tcpSerSock.close()
'''