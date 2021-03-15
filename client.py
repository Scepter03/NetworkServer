import socket
import threading

SERVER = ''
PORT = 5050
ADDRESS = (SERVER, PORT)
HEADERSIZE = 1024
FORMAT = 'utf-8'

alias = input('Enter A Username: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

def clientReceive():
    while True:
        try:
            message = client.recv(HEADERSIZE).decode(FORMAT)
            if message == 'Enter Username:':
                client.send(alias.encode(FORMAT))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break

def clientSend():
    while True:
        message = f'{alias} -----> {input("")}'
        client.send(message.encode(FORMAT))

receiveThread = threading.Thread(target=clientReceive)
receiveThread.start()

sendThread = threading.Thread(target=clientSend)
sendThread.start()
