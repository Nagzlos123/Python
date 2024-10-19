import joblib, os, socket, threading
from tempfile import mkdtemp

"""funkcja zapisuje i odczytuje zawartosc pliku wykorzystujac serializacje za pomoca funkcji joblib """
def file_job():
    date = {"woka":"poka", "sdad":"asd", "dsad":"awds", "as":"ssd"}
    savedir = mkdtemp()
    filename = os.path.join(savedir, 'test.joblib')
    print("Zapisano dane do pliku")
    with open(filename, 'wb') as f: 
        joblib.dump(date, f)
    print("Odczyta zawartosc pliku")
    with open(filename, 'rb') as f:
        print(joblib.load(f))

file_job()

