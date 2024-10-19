import pickle, socket

"""funkcja zapisuje do pliku  slownik wykorzystujac pickle i odczytuje z niego"""
def pick_file():
    dict1 = {"www":"sas", "sas":"aaa", "sas":"sss"}
    pick_out = open("file", "wb")
    print("zapisano do pliku ")
    pickle.dump(dict1, pick_out)
    pick_out.close()
    print("odczytano zawartosc pliku")
    pickle_in = open("file", "rb")
    zawartosc = pickle.load(pickle_in)
    print(zawartosc)
pick_file()

""" funkcja tworzy serwer ktory odczytuje wiadomosc wysylywane przez klienta dane sa odcztytywane za pomocu 
pickle"""
def server_pickle():
    print("\nSerwer zaczyna nasluchiwanie.....")
    HOST = 'localhost'
    PORT = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Klient polaczyl sie z serwerem', addr)
    data = conn.recv(4096)
    data_variable = pickle.loads(data)
    conn.close()
    print('Dane otrzymane od klienta')
    print(data_variable)

"""prosty przyklad wykorzystujace pickle"""
def example_pickle():
    Omkar = {'key' : 'Om', 'na' : 'Om Pat','a' : 2, 'p' : 40000}
    serial_ex = pickle.dumps(Omkar)
    received = pickle.loads(serial_ex)
    print("\n ", received)

example_pickle()
server_pickle()
