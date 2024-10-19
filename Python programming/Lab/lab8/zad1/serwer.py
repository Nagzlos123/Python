#!/usr/bin/env python3
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = 'localhost'
PORT = 40000  
server_adress= (HOST, PORT)
print("Serwer wystartowal na adresie {} i porcie {}".format(*server_adress))
sock.bind(server_adress)

while True:
    print("Serwer czeka na  otrzymanie wiadomosc ")
    data, address = sock.recvfrom(4096)
    print("Serwer otrzymal wiadomosc  {} o rozmiarze {}".format(address, len(data)))
    print("Tresc wiadomosc: {} ".format(data))
    if data: 
        odp_serwera = b"Odpowiadam "
        sent = sock.sendto(odp_serwera, address)
        print("Serwer wyslal wiadomosc do {}".format(address))

