#!/usr/bin/env python3
from matplotlib import pylab
from pylab import * 

def pr1():
    """
    przyklad na poczatku tworzy macierz 10x10 zapisuje ja w zmiennej
    potem tworzy na jej podstawie macierz wypelnionej zerami 
    nastepnie za pomoca dwoch petli iteruje po macierzy a
    ,podczas dzialanie petli sa  przypisywane 
    wartosc macierzy a do macierzy b  
    """
    a = eye(10)
    b = zeros(a.shape)
    for w in list(range(a.shape[0])):
        for k in list(range(a.shape[1])):
            print(w,k)
            b[w,k] = a[w,k]

def pr2():
    """
    przyklad na poczatku tworzy macierz 10x8 ktora zapisuje do zminnej a
    nastepnie elementa  od indeksie 3 i 5 w calej macierzy sa przypisywane wartosc 1
    na podstawie macierzy a tworzona jest tworzona macierz b ktore jest zerowana
    na koncu sa petla ktora ma za zadanie wypelnij macierz b  tak samo jak macierz a
    """
    a = zeros((10,8))
    a[:,(3,5)] = 1
    b = zeros(a.shape)
    for w in range(a.shape[1]):
        for k in range(a.shape[1]):
            print(w,k)
            b[w,k] = a[w,k]
    imshow(b, interpolation='none',cmap='Blues')

def pr3():
    """
    przyklad na poczatku tworzy macierz 11x9 i zapisuje ja do zmiennej a
    a nastepnie w rzedach 5 i  8 , w kolumnach 0 , 3, 6   sa przypisywane 1
    nastepnie na bazie utworzonej macierzy jest tworzona nowa macierz
    nastepnie dzieki petli  i list komprahetnych wypelniona jest macierz tak samo jak a 
    """
    a = zeros((11,9))
    a[5::3,0:8:3] = 1
    b = zeros(a.shape)
    for (y,x) in [(y,x) for y in range(a.shape[0]) for x in
    range(a.shape[1]) if a[y,x]>0.5]:
        print(y,x)    
        b[y,x]=a[y,x]
    imshow(b,interpolation='none',cmap=cm.gray)

def pr4():
    """
    przyklad na poczatku tworzy macierz 11x9 i zapisuje ja do zmiennej a
    a nastepnie w rzedach 5 i  8 , w kolumnach 0 , 3, 6   sa przypisywane 1
    nastepnie na bazie utworzonej macierzy jest tworzona nowa macierz
    dalej wykorzystujac  petle wraz z iteratorem ndindex robi to samo co  przyklad 3
    """
    a=zeros((11,9))
    a[5::3,0:8:3]=1
    b=zeros(a.shape)
    for y,x in ndindex(a.shape):    
        print (y,x)    
        b[y,x]=a[y,x]
    print(b)
    imshow(b,interpolation='bilinear',cmap=cm.hot)

def pr5():
    """
    przyklad tworzy macierz 11x9
    nastepnie przypisuje wartosc 1 co drugiemu rzedowi i kolumnie
    potem na podstawie macierzy a tworzy macierz b  ktore jest wyzerowana 
    na koncu dzieki itertorowi ndumerate ktory przyjmuje macierz a i petli 
    przypisuje wartosc z macierz a do macierzy b 
    """
    a=zeros((11,9))
    a[::2,::2]=1
    b=zeros(a.shape)
    for (y,x),i in ndenumerate(a):    
        print(y,x,i)    
        b[y,x]=a[y,x]
    imshow(b,interpolation='none',cmap=cm.autumn)

def pr6():
    """
    przyklad tworzy tuple o nazwie mytuple
    nastepnie tworzy iterator myit ktory bedzie iterowal po tupli 
    na koncu wyswietla nastepne elementy tupli za pomoca metody next()
    """
    mytuple = ("apple", "banana", "cherry")
    myit = iter(mytuple)
    print(next(myit))
    print(next(myit))
    print(next(myit))

def pr7():
    """
    przyklad na poczatku tworzy klase MyNumbers ktore bedzie  naszym nowym iteratorem
    klasa zawiera dwie metody ktore bede nam potrzebne aby stworzy swoj iterator __iter__() i __next__() . 
    iter zwraca iterator i tworzy wlasciwosc  o nazwie a , a next sluzy do iterowanie w naszym przypadku  
    podnosi  atrybut a o 2 przy kazdym wywolanie
    potem tworzy obiekt myclass na podstawie klasy Mynumbers
    .Na koncu wykorzystujac metode iter tworzy iterator obiektu myclass 
    """
    class MyNumbers:  
        def __iter__(self):    
            self.a = 1    
            return self  
        def __next__(self):   
            x = self.a  
            self.a += 2    
            return x
    myclass = MyNumbers()
    myiter = iter(myclass)
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))

def pr8():
    """
    przyklad robi to samo co przyklad  wyzej ale  totako wewnatrz metody  __next__ jest instrukcja warunkowa
    if else . w if jest warunek ze wartosc atrybut a nie moze byc wieksza niz 20 w przeciwynym wypadku 
    zglosi wyjatek StopIteration . Dodatkowo teraz wkorzystuje petle do iterowanie  wyswietlajac kolejne 
    liczby zwiekszane o dwa, dopóki liczba nie bedzie wieksza od 20  
    """
    class MyNumbers:
        def __iter__(self):
            self.a = 1  
            return self 
        def __next__(self): 
            if self.a <= 20: 
                x = self.a   
                self.a += 2     
                return x  
            else: 
                raise StopIteration
    myclass = MyNumbers()
    myiter = iter(myclass)
    for x in myiter: 
        print(x)

def pr9():
    """
    przyklad liczy  koljene wyrazy ciagu fibonaiego 
     W tym celu  zostaje utworzony iterator ktory bedzie liczy kolejne wyrazy 
    ciagu fibonaciego . Max  liczba do ktorgo ma liczyc ten ciag jest podawany przez uzytkownika
    i jest ona inicjaowana przez konsturkor klasy Fib
    
    """
    class Fib:
        def __init__(self, max): 
            self.max = max 
        def __iter__(self): 
            self.a = 0 
            self.b = 1 
            return self

        def __next__(self): 
            fib = self.a 
            if fib > self.max:      
                raise StopIteration   
            self.a, self.b = self.b, self.a + self.b  
            return fib
    liczba = int(input("policz ciag fibaneciego dla tej liczby "))
    fib = Fib(liczba)
    myiter  = iter(fib)
    for x in myiter:
        print(x)


def pr10():
    """
    przyklad ma za zadanie odworcic slowo w tym celu jest utworzony generator reverse ktory przyjmuje slowo 
    jako argument .Generator zwraca kolejne znaki w odwroconej kolejnosc  wykorzystuje w tym celu yield
    """
    def reverse(data):
        for index in range(len(data)-1, -1, -1):
            yield data[index]
    for char in reverse('golf'):
        print(char)

if __name__ == '__main__':
    print("przyklad 1")
    pr1()
    print("przyklad 2")
    pr2()
    print("przyklad 3")
    pr3()
    print("przyklad 4")
    pr4()
    print("przyklad 5")
    pr5()
    print("przyklad 6")
    pr6()
    print("przyklad 7")
    pr7()
    print("przyklad 8")
    pr8()
    print("przyklad 9")
    pr9()
    print("przyklad 10")
    pr10()
