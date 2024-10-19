#!/usr/bin/env python3
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = 'localhost'
PORT = 40000
server_address = (HOST, PORT)
wiadomosc = b" Klienta wiadomosc to jest"
try:
    print("Klient wysylala wiadomosc do serwera")
    sent = sock.sendto(wiadomosc, server_address)
    print("Klient czeka na wiadomosc od serwera")
    data, server = sock.recvfrom(4096)
    print("Klienta otrzymal wiadomosc od serwra")
    print('Tresc wiadomosc: {}'.format(data))
finally:
    print("Klient zakonczyl komunikacje z serwerem")
    sock.close()
