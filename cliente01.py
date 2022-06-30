import socket

HOST = '127.0.0.1'
PORTA = 2343

s = socket.socket()
s.connect((HOST, PORTA))
print('conectado\n')
namefile = str(input('Arquivo :'))
s.send(namefile.encode())
with open(namefile, 'wb') as file:
    while 1:
        data = s.recv(10000)
        if not data:
            break
        file.write(data)
print(f'{namefile} recebido')

