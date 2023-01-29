#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
# ����һ�������
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',8848)) #��Ҫ�����Ķ˿�
server.listen(5) #��ʼ���� ��ʾ����ʹ����������Ŷ�
while True:# conn���ǿͻ������ӹ������ڷ����Ϊ�����ɵ�һ������ʵ��
    conn,addr = server.accept() #�ȴ�����,������ӵ�ʱ��ͻ��������,��ʵ����������ֵ
    print(conn,addr)
    while True:
        try:
            data = conn.recv(1024)  #��������
            print('recive:',data.decode()) #��ӡ���յ�������
            conn.send(data.upper()) #Ȼ���ٷ�������
        except ConnectionResetError as e:
            print("ds")
            break
    conn.close()