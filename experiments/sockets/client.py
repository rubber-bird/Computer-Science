#!/usr/bin/python3

import socket 
HOST = '0.0.0.0'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b'HIIII!')
	data = s.recv(1024)

print('Received', repr(data))
