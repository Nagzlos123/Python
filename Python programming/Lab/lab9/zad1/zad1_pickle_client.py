import pickle, socket

""" funkcja tworzy klienta ktory bedzie zapisyweal wiadomosc wykorzystujac pickle """
def client_pickle():
    HOST = 'localhost'
    PORT = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    variable = "tekstowa wklienta"
    data_string = pickle.dumps(variable)
    s.send(data_string)
    s.close()
    print ('Wyslano wiadomosc do klienta')

client_pickle()
