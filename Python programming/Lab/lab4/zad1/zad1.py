#!/usr/bin/env python3
from abc import ABC, abstractmethod

def example1():
    """
    przyklad tworzy klas Person ktorej konstruktor przyjmuje dwa argumenty .Dodatkowo klasa zawiera metode
    printname ktora wypisuje na ekran przyjete w konstruktorze argumenty
    .Do przykladem dodalem kolejny argumenty ktory bedzie przyjmowal konstruktor klasy i zmienna 
    ktora bedzie miec przypisana wartosc tego arguemntu , ponadto dodalem drugi obiekt klasy 
    """
    class Person:
        def __init__(self, fname, lname, age):
            self.firstname = fname
            self.lastname = lname
            self.age = age
        def printname(self):
            print(self.firstname, self.lastname, self.age)

    p1 = Person("John", "Doe" ,33)
    p1.printname()
    p2 = Person("Gary", "Tesco", 22)
    p2.printname()

def example2():
    """
    przyklad jest podobny do poprzedniego tylko dodano klasa pochodna Student ktora dziedziczy po klasie 
    Person. Dodalem dodatkowa klase ktora dziedziczy po klasie Person
    i obiekt ktory jest tworzony na podstawie tej klasy
    """
    class Person:
        def __init__(self, fname, lname):
            self.firstname = fname
            self.lastname = lname
        def printname(self):
            print(self.firstname, self.lastname)
    class Student(Person):
        pass
    class Profesor(Person):
        pass
    x = Student("Mike", "Olsen")
    x.printname()
    y = Profesor("Miroslaw", "Blow")
    y.printname()

def example3():
    """
    przyklad tworzony pusta klasa  test ktora dziedzicy po klasie object , potem tworzy na jej
    podstawie obiekt t ktoremu przypisywana jest wlasciwosc  o nazwie a przyjmuja wartosc 10
    Na koncu uzywamy dir aby wyswietic atrybytu i metody obiektu 
    Dodatkowo dwie nowej wlasciwosc do obiektu t
    """
    class test(object):
        pass
    t = test()
    t.a = 10
    print(t.a)
    print(dir(test))
    t.b = 20
    t.c = "www"
    print(t.b)
    print(t.c)
    print(dir(test))

def example4():
    """
    przyklad tworzy klasy pusta Foo  w sposob dynamiczny wykorzystujac funkcje type()
    o na koncu jest  wyswieltane obiekt klasy
    .Utworzylem dwie klasy w sposob dynamiczny
    """
    Foo = type('Foo', (), {})
    x = Foo()
    Kawa = type('Kawa', (), {})
    Naz = type('Naz', (), {})
    print(x)
    y = Kawa()
    z = Naz()
    print(y)
    print(x)

def example5():
    """
    przyklad tworzy dwie klasy (Foo, Bar) za pomoca type() ,jedna klasa dziedzicy po drugie
    Klasa Bar ma zdefiniowany wlasciwosc attr przyjmujaca wartosc 100.Na koncu jest tworzony obiekt x 
    a nastepnie jest wyswietlany zawartosc attr a potem jaka klasa jest potomna a nastpnie jaka klasa 
    jest bazowa Dodalem dodatkowy atrybut do klas Bar, utworzylem dwie klasy za pomoca 
    type jedna dziedziczy po drugiej i po klasie Bar
    """
    Foo = type('Foo', (), {})
    Bar = type('Bar', (Foo,), dict(attr=100, ww=200))
    x = Bar()
    print(x.attr)
    print(x.ww)
    print(x.__class__)
    print(x.__class__.__bases__)
    Klas = type('Klas', (), dict(woka="sss", poka="qaw"))
    Kub = type('Kub', (Klas, Bar, ),{})
    test = Klas()
    print(test.woka)
    print(test.__class__)
    print(test.__class__.__bases__)
    print(Klas.__subclasses__())

def example6():
    """
    przyklad tworzy dwie klasy jedna dziedziczy po drugiej.Klasa bazowa w konstruktorze ma parametr mamalName
    i wewnatrz konstruktora  jest wyswietlany text wraz z wprowadzonym wartoscia w argumencie w
    tym przypadku wartosc jest pusta Nastepnie klasa potomna dziedzica po klasie bazowej  i wykorzystujac
    funkcje super() odwolujemy sie do klasy bazowej 
    Dodalem dodatkowo klasa ktora dziedziczy po klasie Dog  .Nowa klasa odwoluje sie za pomoca 
    funckji super()  do  klas Dog 
    """
    class Mammal(object):
        def __init__(self, mammalName):
            print(mammalName, 'is a warm-blooded animal.')

    class Dog(Mammal):
        def __init__(self):
            print('Dog has four legs.')
            super().__init__('Dog')
    
    class Owczarek(Dog): 
        def __init__(self):
            super().__init__()
            print("jej numa jej klasa Owczarek")
    
    w = Owczarek()

def example7():
    """
    przyklad tworzy 3 klasy klasa dziedzidzy po dwoch klasach A i B . Za pomoca fukncji super() moze zobaczyc 
    w jakiej kolejnosc beda wywolywane metody  klas 
    Dodalem dodatkowa klase D po ktorej bedzie dziedzic C . Umiescilem to klasa jako druga  po ktorej 
    bedzie dziedziczyla klasa C. Co spowodowalo ze metody klasy D jest wywolana jako druga 
    """
    class A(object):
        def __init__(self):
            super(A, self).__init__()
            print( 'init A' )
    class B(object):
        def __init__(self):
            super(B, self).__init__()
            print( 'init B' )
    class D(object):
        def __init__(self):
            super(D, self).__init__()
            print( 'init D' )
    class C(A,D,B):
        def __init__(self):
            super(C, self).__init__()
            print( 'init C' )
    c = C()

def example8():
    """
    przyklad pokazuje jakiej kolejnosc bede wywolywane metoda klas
    Dodalem dodatkowa klasa po ktorej bedzie dziedziczyla klasa D
    """
    class A(object):
        def foo(self, call_from):
            print ("foo from A, call from %s" % call_from)
            super().foo("A")
    class B(A):
        def foo(self, call_from):
            print ("foo from B, call from %s" % call_from)
            super().foo("B")
    class C(A):
        def foo(self, call_from):
            print ("foo from C, call from %s" % call_from)
            super().foo("C")
    class F(object):
        def foo(self, call_from):
            print ("foo from F, call from %s" % call_from)
    class G(object):
        def foo(self, call_from):
            print ("foo from G, call from %s" % call_from)
    class D(B, C, F, G):
        def foo(self):
            print ("foo from D")
            super().foo("D")
    d = D()
    d.foo()
    print( D.__mro__ )

def example9():
    """
    przyklad tworzy pseudoklasa abstrakcyjna (klasa ktora nie jest klasa abstrakcyjna)
    ktora ma metoda ktora nic nie robi . Po tej klasie dziedziczy klasa B
    Dodalem kolejna klase ktora tez bedzie dziedzic po klasie AbstractClassExample
    """
    class AbstractClassExample():
        def do_something(self):
            pass
    class B(AbstractClassExample):
        pass
    class C(AbstractClassExample):
        pass
    a = AbstractClassExample()
    b = B()
    c = C()
    print("klasa nic nie robi ")

def  example10():
    """
    przyklad tworzy klasa abstrakcyjna i nastepnie dwie klasy dziedziczace po niej  jedna dodaje do zmiennej 
    value 42  o druga mnozy wartosc zmiennej valueo 42  
    Dodalem  kolejna klasa ktore dziedziczy po klasie abstrakcyjnej AbstractClassExample ktore odejmuje 20
    """
    class AbstractClassExample():
        def __init__(self, value):
            self.value = value
            super().__init__()
        @abstractmethod
        def do_something(self):
            pass
    class DoAdd42(AbstractClassExample):
        def do_something(self):
            return self.value + 42
    class DoMul42(AbstractClassExample):
        def do_something(self):
            return self.value * 42
    class DoSub20(AbstractClassExample):
        def do_something(self):
            return self.value - 20
    x = DoAdd42(10)
    y = DoMul42(10)
    z = DoSub20(20)
    print(x.do_something())
    print(y.do_something()) 
    print(z.do_something()) 

def example11():
    """
    przyklad tworzy klase z abstrakcyjna z metoda abstrakcyjna do_something 
    klasa anaotherSubclass dziedzicy po klasie abstraykcyjne i tworzy wlasna wersje metody do-someting
    w ktorej wywoluje wersje metody z klasy abstrakcyjne za pomoca funkcji super() dodatkowa wypsuje 
    komunikat
    .Dodalem kolejna metode abstrakcyjna i jej implementacje
    """
    class AbstractClassExample():
        @abstractmethod
        def do_something(self):
            print("Implementacja metody abstrakcyjnej ")
        def kirita_meme(self):
            print("Soa jest slabe")

    class AnotherSubclass(AbstractClassExample):
        def do_something(self):
            super().do_something()
            print("Metoda dziedzicząca")
        def kirita_meme(self):
            super().kirita_meme()

    x = AnotherSubclass()
    x.do_something()
    x.kirita_meme()

def example12():
    """
    przyklad tworzy klase ktorej obiekt jest deksryptor dany ktory wypisuje komunikat po kazdej operacji 
    .przypisałem atrybutowi name nowa wartosc potem ja wyswietlilem a na koncu usunolem
    """
    class Descriptor:
        def __init__(self):
            self.name = ''
        def __get__(self, instance, owner):
            print ("Getting: %s" % self._name)
            return self._name
        def __set__(self, instance, name):
            print("Setting: %s" % name)
            self._name = name.title()
        def __delete__(self, instance):
            print("Deleting: %s" %self._name)
            del self._name

    class Person:
        name = Descriptor()

    user = Person()
    user.name = 'john smith'
    print(user.name)
    del user.name
    user.name = 'Janusz Mikke'
    print(user.name)
    del user.name

def example13():
    """
    przyklad tworzy deskryptor sprawdza ilosc paliwa jesli wartosc jest mniejsza od 0 to wyrzuca wyjatek
    .Dodalem dodatkowy atrybut do klasy Car i zmienilem wartosc
    
    """
    class Descriptor:
        def __init__(self):
            self.__fuel_cap = 0
        def __get__(self, instance, owner):
            return self.__fuel_cap
        def __set__(self, instance, value):
            if isinstance(value, int):
                print(value)
            else:
                raise TypeError("Fuel Capacity can only be an integer")
            
            if value < 0:
                raise ValueError("Fuel Capacity can never be less than zero")
            self.__fuel_cap = value
        def __delete__(self, instance):
            del self.__fuel_caIp

    class Car:
        fuel_cap = Descriptor()
        def __init__(self,make,model,fuel_cap, konie_mh):
            self.make = make
            self.model = model
            self.fuel_cap = fuel_cap
            self.konie_mh = konie_mh
        def __str__(self):
            return "{0} model {1} with a fuel capacity of {2} ltr. {3} mh".format(self.make,self.model,
                    self.fuel_cap, self.konie_mh)
    car2 = Car("Audi","B6",40,220)
    print(car2)

def example14():
    """
    przyklad tworzy deskrytor ktora wypisuje odpowiednie komunikat gdy zostanie  zaktualizowana wartosc 
    wlasciwosc x  Dodalem sprawdzanie czy wartosc x istnieje przed jej wypisaniem 
    """
    class RevealAccess:
        """A data descriptor that sets and returns valuesnormally and prints a message logging their access."""
        def __init__(self, initval=None, name='var'):
            self.val = initval
            self.name = name
        def __get__(self, obj, objtype):
            print('Retrieving', self.name)
            try:
                return self.val
            except:
                print("Var x nie jest zadeklarowana")
        def __set__(self, obj, val):
            print('Updating', self.name)
            self.val = val

    class MyClass:
        x = RevealAccess(10, 'var "x"')
        y = 5

    m = MyClass()
    print(m.x)
    m.x = 20
    print(m.x)
    print(m.y)
    m.x= "q"

def main():
    print("przyklad 1")
    example1()
    print("\nprzyklad 2")
    example2()
    print("\nprzyklad 3")
    example3()
    print("\nprzyklad 4")
    example4()
    print("\nprzyklad 5")
    example5()
    print("\nprzyklad 6")
    example6()
    print("\nprzyklad 7")
    example7()
    print("\nprzyklad 8")
    example8()
    print("\nprzyklad 9")
    example9()
    print("\nprzyklad 10")
    example10()
    print("\nprzyklad 11")
    example11()
    print("\nprzyklad 12")
    example12()
    print("\nprzyklad 13")
    example13()
    print("\nprzyklad 14")
    example14()

main()
