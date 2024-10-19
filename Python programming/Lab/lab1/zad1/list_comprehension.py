#!/usr/bin/env python3
from matplotlib import pylab
from pylab import *

def ex1():
    """
    przyklad wykorzystujac
    liste komprahetna zwraca potegi liczb zawartych w liscie a nastepnie print()  wyswietlana  je 
    """
    print([x * x for x in [1, 2, 3, 4] ])

def ex2():
    """
    przyklad  wyswietla liczby mniejsze od 0   robi to na dwa sposoby wykorzystujac  listy komprahetne i 
    programowanie funkcyjne 
    """
    x = range(-5, 5)
    all_less_than_zero = list(filter(lambda num: num < 0, x))
    print(all_less_than_zero)
    x = range(-5, 5)
    all_less_than_zero  =[num for num in  x if num < 0]
    print(all_less_than_zero)

def ex3():
    """
    progeam wyswietla macierz dwu elementowa  ktorego wartosc z lewej  sa podnoszone o dwa
    za pomoca listy comprahetnej ktorej znajduja sie dwie petle ktore jedna iteruje po jednej czesc macierzy a druga po drugiej czesci macierzy 
    """
    a = zeros((10,8))
    a[::2,:]=1 
    b=zeros(a.shape)
    for (y,x) in [(y,x) for y in range(a.shape[0]) for x in range(a.shape[1]) if a[y,x]>0.5]:   
        print(y,x)   
        b[y,x]=a[y,x]
    imshow(b,interpolation='none',cmap=cm.gray)
def ex4():
    """
    program dzieli zagniezdzona liste  na mniejsze czesci 
    """
    trasposed = []
    matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
    for i in range(len(matrix[0])):
        trasposed_row = []
        for row in matrix:
            trasposed_row.append(row[i])
        trasposed.append(trasposed_row)
    print(trasposed) #[[1, 4], [2, 5], [3, 6], [4, 8]]


def ex5():
    """
    przyklad tworzy liste w liscie 
    nastepnie tworzy liste wykorzystujac zagniezdzone listy comprahetne
    na poczatku petla liczy do dwoch wartosc kazdej iteacji tej petli jest przekazywana
    jest przekazywana do zagniezdzonej listy ktora wybiera elementy o takim samy indeksie 
    tworzy z nich liste taka utworzona liste wyswietla na ekranie
    """
    matrix = [[1, 2], [3,4], [5,6], [7,8]]
    transpose = [[row[i] for row in matrix]  for i in range (2)]
    #it 1 [ [1,3,5,7] ]
    #it 2 [ [1,3,5,7] , [2,4,6,8]]
    print(transpose) #[[1, 3, 5, 7], [2, 4, 6, 8]]
    
def ex6():
    """
        przyklad na poczatku przydziela do zmiennej x wartosc od - 5 do 5
        nastepnie tworzy liscte all_less_than_zero do ktorej za pomoca wyrazenie lambda i  funkcji filter
        sa wybierane  liczby mniejsze od 0 a nastepnie  za pomoca funkcji map i lambdy   
        sa one podnoszone do kwadratu 
        utworzona lista jest wyswietlana na ekranie
    """
    x = range(-5,5)
    all_less_than_zero = list(map (lambda num: num * num,
    list(filter(lambda num: num <0, x))))
    print(all_less_than_zero) #[25, 16, 9, 4, 1]

def ex7():
    """
    przyklad  tworzy  liste 
    nastepnie tworzy liste o nazwie all_less_than_zero  do ktorej sa zapisywane wartosc mniejsze od zera 
    ktore sa podnoszone do kwadratu
    a na koncu jest wyswietlana  nowo utworzona lista
    """
    x = range(-5 ,5)
    all_less_than_zero =[num * num for num in x if num < 0]
    print(all_less_than_zero) #[25, 16, 9, 4, 1]

def ex8():
    """
    przyklad tworzy list fruits  potem w nastepnej intrukcja 
    sprawdza  iterujac po petli jakie elementy zawiera litery a i e lub k
    potem w trakcie dzialania petli sprawdza czy  podany element ma wartosc 'apple' jesli tak to przyposuje
    mu wartosc orange a jesli nie to zwraca go normalnie a na koncu wyswietla nowo utworzona  liste
    """
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    print([(x if x != "apple" else "orange") for x in fruits if 'a' in x and'e' in x or 'k' in x])
    #['orange', 'kiwi']

def ex9():
    """
    przyklad wyswietla na dwa sposoby elementy listy zaczynac kazdy z nich z  duzej litery  
    """
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    print( [f[0].upper()+f[1:] for f in fruits] ) #['Apple', 'Banana', 'Cherry', 'Kiwi', 'Mango']
    print( [f.capitalize() for f in fruits] )  #['Apple', 'Banana', 'Cherry', 'Kiwi', 'Mango']

def ex10():
    """
    przyklad tworzy tuple w liscie  o nazwie dial_codes
    nastepnie za pomoca list comprehension jest tworzono od zmiennej dial_codes  slownik country_code
    nastepny jest on wyswietlany
    na koncu jest wyswietlane klucz i wartosc slownika . Wartosc jest v wyswietlana duzymi literami 
    .Wyswietlanie sa tylko  te wartosc gdzie klucz jest mniejszy od 66
    """
    DIAL_CODES = [ (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan')
    ]
    country_code = {country: code for code, country in DIAL_CODES}
    print(country_code) #{'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 
    #'Pakistan': 92, 'Bangladesh': 880, 'Nigeria': 234, 'Russia': 7, 'Japan': 81}
    print({code: country.upper() for country, code in country_code.items() if code <66})
    #{1: 'UNITED STATES', 62: 'INDONESIA', 55: 'BRAZIL', 7: 'RUSSIA'}

def ex11():
    """
    przyklad tworzy slownik  a nastepnie przypisuje  klucze od 1 do 10  i  wartosc podnoszac je do 
    kwadratu . Robi to na  dwa sposoby 
    """
    square_dict = dict()
    for num in range(1, 11):
        square_dict[num] = num * num
    print(square_dict)
    
    square_dict = {num: num * num for num range(1,11)}
    print(square_dict)

if __name__ == '__main__':
    print("przyklad 1 ")
    ex1()
    print("przyklad 2 ")
    ex2()
    print("przyklad 3 ")
    ex3()
    print("przyklad 4 ")
    ex4()
    print("przyklad 5 ")
    ex5()
    print("przyklad 6 ")
    ex6()
    print("przyklad 7 ")
    ex7()
    print("przyklad 8 ")
    ex8()
    print("przyklad 9 ")
    ex9()
    print("przyklad 10 ")
    ex10()
    print("przyklad 11 ")
    ex11()
