import socket, sys , json
"funkcja zapisuje dane w postaci json do pliku a potem jest odczytuje"
def file_json():
    data = {"menu": {"id": "file","value": "File","popup": {"menuitem": 
        [{"value": "New", "onclick": "CreateNewDoc()"},{"value": "Open", "onclick": "OpenDoc()"}]}}}
    print("Zapisywanie do pliku")
    with open('file_json', 'w') as f:
        json.dump(data, f, sort_keys=True)
    print("Odczytywania zawartosc pliku")
    with open('file_json', 'r') as f:
        data = json.load(f)
    print(data,"\n")

file_json()
"""
funkcja pokazuje przyklad demostrujacy proste wykorzystanie biblioteki json
"""
def ex_json():
    date =  '{ "nam":"Joh", "ag":23}'
    datwe_json = json.loads(date)
    print(datwe_json)
ex_json()

def server_json():
    print("\nServer nalsluchuje.....")
    HOST = 'localhost'
    PORT = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Klinet polaczyl sie ', addr)
    data = conn.recv(4096)
    data_variable = json.loads(data)
    conn.close()
    print('Wiadomosc wyslana przez klienta')
    print(data_variable)

server_json()
