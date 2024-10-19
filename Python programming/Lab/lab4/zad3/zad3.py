#!usr/bin/env python3
"""
wedlug moim obserwacji bez problemu mozna sie odwolywac do pierwszej klasy z do najnizszej klasy
(dziedziczy po wszystkich innych klasach w schemacie dziedziczenia)
Klasy zostaje wywolane pokolej
"""
class Klasa_odlegla(object):
    def __init__(self):
        print("Klasa odlegla ")
    def testowanie5():
        print("test odlegla")

class Klasa_A(object):
    def __init__(self):
        print("Klasa A")
    def testowanie():
        print("test A")

class Klasa_B(Klasa_A):
    def __init__(self):
        Klasa_A.__init__(self)
        print("Klasa B")
    def testowanie2():
        print("test B")

class Klasa_C(Klasa_B):
    def __init__(self):
        Klasa_B.__init__(self)
        print("Klasa C")
    def testowanie3():
        print("test C")

class Klasa_D(Klasa_C):
    def __init__(self):
        Klasa_C.__init__(self)
        print("Klasa D")
    def testowanie4():
        print("test D")

class KlasaE(Klasa_D, Klasa_odlegla):
    def __init__(self):
        Klasa_D.__init__(self)
        Klasa_odlegla.__init__(self)
        print("Klasa E")
        Klasa_odlegla.testowanie5()
        Klasa_D.testowanie4()
        Klasa_A.testowanie()
        
    

print("od klasy b ")
b = Klasa_B()
print("od klasy c ")
c= Klasa_C()
print("od klasy e")
e = KlasaE()
