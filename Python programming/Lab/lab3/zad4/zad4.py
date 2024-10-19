#!/usr/bin/env python3
from more_itertools import chunked, distribute, spy, intersperse , padded, ncycles
def pr1():
    """
    przyklad wykorzystuje iterator chunked ktory w tym przypadku  dzieli liste na dwie podlisty
    3 elementowe 
    """
    sl = ["ww","sss","asas", "sddsd", "sas", "asasw"]
    print(list(chunked(sl, 3)))

def pr2():
    """
    przyklad wykorzystuje iterator distribute ktory  w tym przypadku dzieli liste na dwie listy 3 elementowe
    """
    w1, w2 = distribute(2, ["ssdw", "asas", "www", "sawa", "sasw", "cdv"])
    print(list(w1))
    print(list(w2))

def pr3():
    """
    przyklad wykorzystuje iterator spy ktory w tym przypadku przypisuje pierwsza i druga litere slowa
    do zmiennych (fir,sec) a nastepnie wyswietla ich zawartosc
    """
    (fir, sec), sl = spy('Slowokado', 2)
    print(fir)
    print(sec)
    print(list(sl))

def pr4():
    """
    przyklad wykorzystuje iterator intersperse ktory w tym przypadku po 
    kazdym elemencie listy dopisuje jako nastepny element slowo dyktator
    """
    dyktatorzy = ["Francisco Franco", "Idi Amin", "Baszszar al-Asad", "Saddam Husajn", "Mu’ammar al-Kaddafi"]
    print(list(intersperse('dyktator', dyktatorzy)))
    

def pr5():
    """
    przyklad wykorzystuje iterator padded ktory w tym przypadku dodaje wartosc NONE do listy aby uzyskac
    7 elementow w liscie
    """
    print(list(padded(["www", "sss", "aa"],'None', 7)))

def pr6():
    """
    przyklad wykorzystuje iterator ncycles ktory  w tym przypadku 
    zapisuje dwa razy podrzad wartosc listy o nazwie liczby do nowej listy ktora jest od  razu wyswietlana 
    """
    liczby = [x for x  in range(20) if x % 2 ]
    print("przed ", liczby)
    print("po ", list(ncycles( liczby, 2)))

def main():
    print("przyklad 1 chunked" )
    pr1()
    print("przyklad 2 distribute")
    pr2()
    print("przyklad 3 spy")
    pr3()
    print("przyklad 4 intersperse")
    pr4()
    print("przyklad 5 padded")
    pr5()
    print("przyklad 6 ncycles")
    pr6()

main()
