#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
Created on 2018年2月1日

@author: root
'''
'''
import socket

host,port = '192.168.20.232',18000

s = socket.socket()
s.connect((host,port))
while 1:
    senddata = raw_input("please input data:")
    s.sendall(senddata)
    recvdata = s.recv(1024)
    print recvdata
'''










from socket import *
import threading

HOST = '192.168.20.232'
PORT = 18000
BUFSIZ = 1024
ADDR = (HOST, PORT)
threads = []

def Send(sock, test):
    while True:
        data = raw_input('>')
        tcpCliSock.send(data)
        if data == 'quit':
            break

def Recv(sock, test):
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if data == 'quit':
            sock.close()
            break        
        print data
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

print 'Please input your username:',
username = raw_input()
tcpCliSock.send(username)
data = tcpCliSock.recv(BUFSIZ)
if data == 'Reuse':
    print 'The username has been used!'
else:
    print 'Welcome!'
    chat = threading.Thread(target = Send, args = (tcpCliSock,None))
    threads.append(chat) 
    chat = threading.Thread(target = Recv, args = (tcpCliSock,None))
    threads.append(chat)
    for i in range(len(threads)):
        threads[i].start()
    threads[0].join()
