import socket
import threading

HOST = ''
PORT = 5050
ADDRESS = (HOST, PORT)
HEADERSIZE = 1024
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handleClients(client):
    while True:
        try:
            message = client.recv(HEADERSIZE)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode(FORMAT))
            aliases.remove(alias)
            break

def start():
    while True:
        print('Server is running and listening...')
        client, address = server.accept()
        print(f'Connection is established with {str(address)}')
        client.send('Enter Username:'.encode(FORMAT))
        alias = client.recv(HEADERSIZE)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode(FORMAT))
        client.send('You are now connected!'.encode(FORMAT))

        thread = threading.Thread(target=handleClients, args=(client,))
        thread.start()

if __name__ == "__main__":
    start()


