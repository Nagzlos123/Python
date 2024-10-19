#!/usr/bin/env python3
"""
przyklad tworzy deskryptor przy uzycie funkcji property .Deskryptor sprawdza przy ustawianiu wartosc 
czy tekst jest stringiem czy jest dluzszy od 6
"""
class Descriptor:
    def __init__(self):
        self.__text=''
    def settext(self, text):
        if(isinstance(text,str)):
            if(len(text) > 6):
                print('przpisano  wartosc do atrybutu text')
                self.__text=text
            else:
                raise ValueError("text musi byc dluzszy")
        else:
            raise TypeError("nie mozna przypisac wartosc bo nie jest  typu str")
    def gettext(self):
        try:
            print('wyswietlana zawartosc atrybutu text')
            return self.__text
        except:
            print("pole  nie jest zadekralorowane") 
    def deltext(self):
        try:
            print('Usunieto text')
            del self.__text
        except:
            print("pole  nie jest zadekralorowane") 
    text=property(gettext, settext, deltext)

"""
przyklad tworzy deskryptor przy uzyciu funkcji property . deskryptor sprawdza przy przypisywaniu wartosc
czy wartosc jest typu int i czy liczba jest mniejsza od 120
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
            if value  < 120:
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
    p1=Descriptor()
    p1.text="kolcz mike"
    print(p1.text)
    del p1.text
    print("\nprzyklad 2")
    p2 = Descriptor2(33)
    p2.liczba = 5
    print(p2.liczba)
    del p2.liczba

main()
