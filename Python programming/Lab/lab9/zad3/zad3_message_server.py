import socket, sys, msgpack

"""funkcja prezentuje prosty przyklad wykorzystujania MessagePack do serializacji  """
def seriable_msgpack():
    data = {
        "list": [1, 42, 3.141, 1337, "help"],
        "string": "bla",
        "int": 222
    }
    packed = msgpack.packb(data)
    data_loaded = msgpack.unpackb(packed)
    print(data_loaded)

seriable_msgpack()
"""
funkcja tworzy serwer tcp ktory bedzie odbieral wiadomosc od klienta  ktorego wiadomosc 
jest w postaci msgpack
"""
def server_msg():
    print("\nServer Nasluchuje.....")
    HOST = 'localhost'
    PORT = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Klient polaczyl sie', addr)
    data = conn.recv(4096)
    data_variable = msgpack.unpackb(data, use_list=False, raw=False)
    conn.close()
    print('Data received from client')
    print(data_variable)

server_msg()
