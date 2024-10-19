#!usr/bin/env python3
"""
W takiej koljenosc zostaly wywolane klasy
Wywolanie klasy E
Klasa D wywolala Klasa  E
Klasa C wywolala Klasa  D
Klasa B wywolal Klasa  C
Klasa A wywolal Klasa  B
Klasa Klasa_odlegla wywolala Klasa  A
"""
class Klasa_odlegla(object):
    def foo(self, wywolanie):
        print("Klasa Klasa_odlegla wywolala Klase ",wywolanie )
    def testowanie5():
        print("test odlegla")

class Klasa_A(object):
    def foo(self,wywolanie):
        print("Klasa A wywolal Klasa ",wywolanie )
        super().foo("A")
    
    def testowanie():
        print("test A")

class Klasa_B(Klasa_A):
    def foo(self, wywolanie):
        print("Klasa B wywolal Klasa ", wywolanie)
        super().foo("B")
    def testowanie2():
        print("test B")

class Klasa_C(Klasa_B):
    def foo(self, wywolanie):
        print("Klasa C wywolala Klasa ", wywolanie)
        super().foo("C")
    def testowanie3():
        print("test C")

class Klasa_D(Klasa_C):
    def foo(self, wywolanie):
        print("Klasa D wywolala Klasa ", wywolanie)
        super().foo("D")
    def testowanie4():
        print("test D")

class KlasaE(Klasa_D, Klasa_odlegla):
    def foo(self):
        print("Wywolanie klasy E")
        super().foo("E")
        
e = KlasaE()
e.foo()
print(KlasaE.__mro__)
