import socket, sys, msgpack, threading
"""
funkcje ma za zadania wyslac  wiadomosc o roznym typie danych  wykorzystujac biblioteke MessagePack
"""
def client_msg():
    HOST, PORT = "localhost", 50007
    str_w = "as"
    int_t = 111
    fl_t = 22.2
    bol_t = True
    data = msgpack.packb((str_w, int_t, fl_t, bol_t ),  use_bin_type = True)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("klient polaczyl sie z serwerem")
        sock.connect((HOST, PORT))
        print("klient wyslal wiadomosc")
        sock.sendall(data)
    finally:
        sock.close()
client_msg()
