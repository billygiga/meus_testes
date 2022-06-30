import socket


HOST = '127.0.0.1'
PORTA = 2343

s = socket.socket()
s.bind((HOST,PORTA))
s.listen()

c,e = s.accept()
namefile = c.recv(1024).decode()

with open(namefile,'rb') as file:
    for data in file.readlines():
        c.send(data)
    print('arquivo enviado para',e)

