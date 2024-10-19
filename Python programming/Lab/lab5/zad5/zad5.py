#!/usr/bin/env python3
"""
przyklad tworzy deskryptor przy uzycie dekoratora property .Deskryptor sprawdza przy ustawianiu wartosc
czy tekst jest stringiem czy jest dluzszy od 6 . aby oznaczyc odpowiednie metody dekskryptorze uzywamy 
odpowiednich dekoratorow
"""
class Descriptor:
    def __init__(self, text=None):
        self.__text = text
    @property
    def text(self):
        try:
            print('wyswietlana zawartosc atrybutu text')
            return self.__text
        except:
            print("pole  nie jest zadekralorowane")
    @text.setter
    def text(self, text):
        if(isinstance(text,str)):
            if(len(text) > 6):
                print('przpisano  wartosc do atrybutu text')
                self.__text=text
            else:
                raise ValueError("text musi byc dluzszy")
        else:
            raise TypeError("nie mozna przypisac wartosc bo nie jest  typu str")
    @text.deleter
    def text(self):
        try:
            print('Usunieto text')
            del self.__text
        except:
            print("pole  nie jest zadekralorowane")

"""
przyklad tworzy deskryptor przy uzyciu dekoratora property . deskryptor sprawdza przy przypisywaniu wartosc
czy wartosc jest typu int i czy liczba jest mniejsza od 200
"""
class Descriptor2:
    def __init__(self, wartosc=None):
        self.__liczba = wartosc

    def get_liczba(self):
        try:
            return "liczba = {}".format(self.__liczba)
        except:
            print("pole liczba nie jest zadekralorowane")

    def set_liczba(self, value):
        if isinstance(value , int):
            if value  < 200:
                print("Zaktualizowano liczbe ")
                self.__liczba = value
            else:
                raise ValueError("liczba musi byc mniejsza od 120")
        else:
            raise TypeError("liczba musi byc typu int")

    def delete_liczba(self):
            print("Usunieto atrybut liczba")
            try:
                del self.__liczba
            except:
                print("pole liczba nie jest zadekralorowane")
    liczba = property(get_liczba, set_liczba, delete_liczba)

def main():
    print("przyklad 1")
    p1=Descriptor("haha")
    p1.text="ozjasz goldberg"
    print(p1.text)
    del p1.text
    print("\nprzyklad 2")
    p2 = Descriptor2(11)
    p2.liczba = 198
    print(p2.liczba)
    del p2.liczba

main()

