#!/usr/bin/env python3
import socket, sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = 'localhost'
PORT = 40002
server_address = (IP, PORT)
print("Serwer wystartowal {} na porcie {}".format(*server_address))
sock.bind(server_address)
sock.listen(1)
while True: 
    print('Oczekiwanie na połaczenie ze stroną klienta')
    connection, client_address = sock.accept()
    try:
        print("Klient polaczyl sie z serwerem z ", client_address)
        while True:
            data = connection.recv(16)
            print('Serwer otrzymal wiadomosc od klienta "%s"' % data)
            if data: 
                print('Wysłano wiadomosc zwrotna do klienta')
                connection.sendall(data)
            else:
                print('Nie ma żadnych  wiadomosc od klienta', client_address)
                break
    finally:
        print("Klient zakonczyl prace")
        connection.close()


