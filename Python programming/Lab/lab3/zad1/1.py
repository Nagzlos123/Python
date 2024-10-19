#!/usr/bin/env python3
import itertools
def pr1():
    """
    program wypisuje wartosc w asci znakow znajdujacych sie w tablicy (dodalem kolejne elementy do tablicy)
    """
    unique_characters= ('E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y', '2', '3', 'Q')
    gen = (ord(c) for c in unique_characters)
    print(gen)
    print(next(gen))
    print(next(gen))
    print(tuple(ord(c) for c in unique_characters))

def pr2():
    """
    wyswietla kolejne  permutacje liczb od 1-4 wyswietlajac kazda permutacje w zbiorach trzech elementowych
    """
    perms = itertools.permutations([1,2,3,4],3)
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(list(itertools.permutations([1,2,3,4],3)))

    
def pr3():
    """
    wyswietla kolejne permutacje liter ABCDE w zbiorach pieco elementowych
    """
    perms = itertools.permutations('ABCDE',5)
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(next(perms))
    print(list(itertools.permutations('ABCDE',5)))

def pr4():
    """
    przyklad liczy iloczyn ABCDE i 123 (laczy pierwszy arugument z drugim argument iterarujac po nim )
    przyklad 2 wypisuje kombinacje zbioru ABC
    """
    print(list(itertools.product('ABCDE', '123')))
    print(list(itertools.combinations('ABC', 2)))
    
def pr5():
    """
    przyklad sortuje i gropuje elementy znajdujace sie w liscie names 
    """
    names=('Dora  ','Ethan  ','Wesley  ','John  ','Anne  ','Mike  ','Chris  ','Sarah  ','Alex  ','Lizzie  '
            ,'Kasia', 'Ola', 'Wikora', 'Anna', 'Nikodem')
    print(names)
    names = [name.rstrip() for name in names]
    print(names)
    names = sorted(names)
    print(names)
    names = sorted(names, key=len) 
    print(names)
    groups = itertools.groupby(names, len) 
    print(groups)
    print(list(groups))
    groups = itertools.groupby(names, len) 
    for name_length, name_iter in groups:     
        print('Names with {0:d} letters:'.format(name_length))    
        for name in name_iter:        
            print(name)


def pr6():
    """
    przyklad tworzy deskrytor ktora wypisuje odpowiednie komunikat gdy zostanie usunieta wartosc lub
    zaktualizowana wartosc wlasciwosc x  obiektu Myclass 
    """
    class MyDescriptor(object):    
        """A data descriptor that sets and returns values       
        normally and prints a message logging their access.    
        """
        def __init__(self, initval=None, name='var'):  
            self.val = initval        
            self.name = name    
        def __get__(self, obj, objtype): 
            print('Retrieving', self.name)    
            try:      
                return self.val  
            except:           
                print('Var x is not declared')    
        def __set__(self, obj, val):   
            print('Updating', self.name)   
            self.val = val   
        def __delete__(self, obj):    
            print('Deleting', self.name)  
            try:      
                del self.val    
            except:      
                print('Var x is not declared')
    class MyClass(object):
        x = MyDescriptor("ww", 'var "x"')
        y = "www"
    m = MyClass()
    print(m.x)
    m.x = "qxxx"
    print(m.x)
    print(m.y)
    del m.x
    print(m.x)
    m.x= "q"
    print(m.x)
    del m.x
    print(m.x)

def pr7():
    """
    przyklad tworzy deskrytor  kotry wyswietla wartosc wlasciwosc name 
    podwojnie i dodatkowo umieszcza pomiedzy nimi slowo 
    .atrybut name  przyjmuje jedynie string jesli nie bedzie to string wyrzuca wyjatek
    """
    class Descriptor(object):
        def __init__(self, name =''):
            self.name = name
        def __get__(self, obj, objtype):
            return "{}druga_ciag{}".format(self.name, self.name)
        def __set__(self, obj, name):
            if isinstance(name, str): 
                self.name = name
            else:
                raise TypeError("Name should be string") 
    class GFG(object): 
        name = Descriptor() 
    g = GFG()
    g.name = "Computer_www_ww"
    print(g.name) 
    #g.name = 1
    #print(g.name) 

def pr8():
    """
    przyklad tworzy deskryptor sprawdza ilosc paliwa jesli wartosc jest mniejsza od 0 to wyrzuca wyjatek
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
                raise ValueError("Fuel Capacity can never be less thanzero")   
            self.__fuel_cap = value   

        def __delete__(self, instance):   
            del self.__fuel_cap
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

def main():
    print("pr 1")
    pr1()
    print("pr 2")
    pr2()
    print("pr 3")
    pr3()
    print("pr 4")
    pr4()
    print("pr 5")
    pr5()
    print("pr 6")
    pr6()
    print("pr 7")
    pr7()
    print("pr 8")
    pr8()
main()
