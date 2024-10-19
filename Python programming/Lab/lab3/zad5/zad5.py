#!/usr/bin/env python3 

class Descriptor(object):
    """
    deskryptor ma zadanie sprawdzac czy istnieje pole wiek i czy wartosc ktora ma go aktualizowac jest 
    integerem i jest mniejsza od 120
    """
    def __init__(self, wartosc=None):
        self.wiek = wartosc
    
    def __get__(self, obj, objtype):
        try:
            return "osoba ma wiek = {}".format(self.wiek)
        except:
            print("pole wiek nie jest zadekralorowane")

    def __set__(self, instance, value):
        if isinstance(value , int):
            if value  < 120:
                print("Zaktualizowano wiek osoby ")
                self.wiek = value
            else:
                raise ValueError("wiek musi byc mniejszy od 120")
        else:
            raise TypeError("wiek musi byc typu int")
    
    def __delete__(self, obj):
            print("Usunieto atrybut wiek")
            try:
                del self.wiek
            except:
                print("pole wiek nie jest zadekralorowane")
    
class Person(object):
    "klasa okreslaja osobe zawiera pole imie nazwisko i wiek"
    imie = "Tanya"
    nazwisko = "Degurechaff"
    wiek = Descriptor(20)

p = Person()
p.wiek = 5
print(p.wiek)
del p.wiek
