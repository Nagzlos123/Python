#!/usr/bin/env python3
from abc import  ABC , abstractmethod 
"""
przyklad tworzy klasa abstrakcyjne Zwierze od ktorej dziedziczy trzy klasy potomne Slon, Lew, Papuga
i implementuja metode abstrakcyjna przedstaw_sie
"""
class Zwierze(ABC):
    def __init__(self, nazwa, waga):
        self.nazwa = nazwa
        self.waga = waga

    @abstractmethod 
    def nazwa_gatunku(self):
        pass
    def przedstaw_sie(self):
        print("Jestem  Mam na imię {}, mam  wagę {} kg. "
                .format(self.nazwa,  self.waga))

class Slon(Zwierze):
    def nazwa_gatunku(self):
        return "Słoń"

class Lew(Zwierze):
    def nazwa_gatunku(self):
        return "Lew"

class Papuga(Zwierze):
    def nazwa_gatunku(self):
        return "Papuga"

    def __init__(self, nazwa, waga, kolor):
        super().__init__(nazwa, waga)
        self.kolor = kolor

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("Jako papuga mój kolor to ",self.kolor)

def main():
    Dumboo = Slon("Nambo",  6000)
    Simba = Lew("Simba",  100)
    Jago = Papuga("Jago",  20,"czerwony")
    Dumboo.przedstaw_sie()
    Simba.przedstaw_sie()
    Jago.przedstaw_sie()

if __name__ == "__main__":
    main()
