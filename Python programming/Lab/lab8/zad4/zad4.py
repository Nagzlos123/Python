#!usr/bin/env python3 
import ftplib
"""
Program wyswietla zawartosc serwera ftp nastepnie przechodzi do wybranego katalogu wskazanego przez uzytkownika
a na koncu pyta go jaki plik pobrac
"""
def wyswietl_zawartoc_katalogu():
    list_directory = []
    ftp.dir(list_directory.append)
    ftp.quit
    for line in list_directory:
        print("-", line)

def zmien_katalog():
    directory = input("Do ktorego katalogu chcesz przejsc ")
    try:
        ftp.cwd(directory)
    except:
        print("Nie ma takiego katalogu")

def lokalizacja():
    print("Obecny katalog w ktorym jestes ", ftp.pwd())

def pobiez():
    filename = input("Podaj nazwe pliku ktory chcesz scignac ")
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
        print("Pobrano plik")
    except:
        print("Error")

if __name__ == "__main__":
    login = "anonymous"
    haslo = "ftplib-example-1"
    server_ftp = "ftp.nluug.nl"
    ftp = ftplib.FTP(server_ftp)
    ftp.login(login, haslo)
    wyswietl_zawartoc_katalogu()
    zmien_katalog()
    lokalizacja()
    wyswietl_zawartoc_katalogu()
    pobieranie()

    ftp.quit()
