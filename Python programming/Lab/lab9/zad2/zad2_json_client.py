import socket, sys , json
"""
funkcje ma za zadania wyslac i odebrac wiadomosc w postaci formatu json
"""
def network_json():
    HOST, PORT = "localhost", 50007
    m = {"id": 2, "name": "abc"} 
    data = json.dumps(m)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("Klient polaczyl sie z serwerem ")
        sock.connect((HOST, PORT))
        print("Klient wyslal wiadomosc do serwera ")
        sock.sendall(bytes(data,encoding="utf-8"))
    finally:
        sock.close()
network_json()
