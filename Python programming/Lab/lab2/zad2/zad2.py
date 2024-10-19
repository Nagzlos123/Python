#!/usr/bin/env python3
from matplotlib import pylab
from pylab import *

def nindex_przyklad():
    """
    przyklad tworzy macierz  10x10 a nastepnie dzieki iteratorowi ndindex iteruje i przypisuje mu 
    jedenki jesli x jest nieparzyste a jesli jest parzyste to 2
    """
    c = zeros((10,10))
    for x , y in ndindex(c.shape):
        if x & 2 :
            c[x,y] = 1 
        else:
            c[x,y] = 2
    print(c)

def range_pr1():
    """
    przyklad odczytu zawartosc listy(ktora zawiera dwie listy wewnatrz)
    i kazdy jego  elementy podniosi do kwadratu a nastepnie zapisuje go w nowej tablicy
    """
    lista = [ [1,2,3], [3,4,5] ]
    lista2 = []
    for w1 in range(len(lista)):
        for w2 in lista[w1]:
            lista2.append(w2 * w2)
    print(lista2)

def range_pr2():
    """
    przyklad liczyc sume elementow dla kazdej wewnetrznej  listy i zapisuje je w nowej tablicy 
    """
    s2 = 0
    s1 = []
    w = [ [1,2,3,4,5] , [1,2,3,5,6] ] 
    for s in  range(len(w)):
        for z in w[s]:
            s2 += z 
        s1.append(s2)
        s2 = 0
    print("suma obu list w liscie w", s1)

def comprehension_pr():
    """
    przyklad tworzy macierz 10x10 ktory ,nastepnie utworzonej macierzy przypisuje wartosc rzeda od 2 do 8
    .Na podstawie macierzy a tworzona jest macierz b . Macierz a jest literowane za pomoca list comprahetnych
    i petli for  . Wartosc elementow macierz a  ktore sa mnozeno przez wartosc y 
    sa przypisywane  do macierzy b 
    """
    a = zeros((10,10))
    a[::1,2:8] = 2
    b= zeros(a.shape)
    for (y,x) in [(y,x) for y in range(a.shape[0]) for x in range(a.shape[1])]:
        b[y,x] = a[y,x] * y
    print(b)

def ndenumerate_pr():
    """
    przyklad tworzy macierz 10x10 a cnastpenie przypisuje jej 3 co cztery kolumny i rzedy 
    .Potem za pomoca iteratora ndenumerate iterujemy po kolejnych elementach macierz przypisujac je 
    do innej macierzy .Na koncu jest wyswietlana utworzono macierz
    """
    a = zeros((10,10))
    a[::4,::4]= 3
    b = zeros(a.shape)
    for (y,x),i in ndenumerate(a):
        b[y,x] = a[y,x]
    print(b)

def main():
    print("przyklad 1 iterowania po tablicach za pomoca nindex ")
    nindex_przyklad()
    print("przyklad 2 iterowania po tablicach za pomoca range ")
    range_pr1()
    print("przyklad 3 iterowania po tablicach za pomoca range ")
    range_pr2()
    print("przyklad 4 iterowania po tablicach za pomoca comprahetnych list ")
    comprehension_pr()
    print("przyklad 5 iterowania po tablicach za pomoca ndenumerate  ")
    ndenumerate_pr()

main()
