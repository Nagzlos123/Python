import sys,socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = 'localhost'
PORT = 40002
server_address = (IP, PORT)
print("Klient polaczyl z serwerem {} o porcie {}".format(*server_address))
sock.connect(server_address)
try:
    wiadomosc_kl = b'Klient wita'
    print("Klient wyslal wiadomosc do serwera ")
    sock.sendall(wiadomosc_kl)
    amount_received = 0
    amount_expected = len(wiadomosc_kl)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('Klient otrzymal wiadomosc "%s"' % data)
finally:
    print('Klient zakonczyl komunikacje z serwerem')
    sock.close()


