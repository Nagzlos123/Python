#!/usr/bin/env python3
from itertools import count, chain, dropwhile, takewhile, filterfalse, starmap
def itertools_pr1():
    """
    przyklad wykorzystujac iterator count  wyswietla dwanascie liczb po kolej dodajac do nastepnej 3
    """
    count_itr = count(step=3)
    for i in range(12):
        print(next(count_itr)) #0,3,6,9....33

def itertools_pr2():
    """
    przyklad wykorzystuje iterator chain ktora wyswietla zawartosc trzech tablic
    """
    sl = ["ww", "asa", "sss"]
    sl2 = ["as", "sssd", "sas"]
    sl3 = ["dd","dds","sas"]
    for x in chain(sl, sl2, sl3):
        print(x)

def itertools_pr3():
    """
    przyklad wykorzystuje iterator starmap ktory wybiera w tym przypadku najmniejsze wartosc 
    z trzech list znajdujacych sie wewnatrz jednej listy
    """
    liczby = [ [1, 2 ,3], [7,8,2], [88,44,22] ]
    result = starmap(min, liczby)
    print(list(result))

def itertools_pr4():
    """
    przyklad wykorzystuje iterator filterfalse ktory  wyswietla slowo bez liter w ,y i o 
    """
    slowo = "Jaszczurawkowy"
    result = filterfalse(lambda w: w == "w" or w == "y" or w =="o", slowo)
    print(tuple(result))

def itertools_pr5():
    """
    przyklad wykorzystujac iterator takewhile ktory w tym przypadku umieszcza wartosc do listy dopoki 
    nie znajdzie liczby nieparzystej w liscie liczby 
    """
    liczby = [2,4,6,8,10,22,33,11,23,25,28]
    result = takewhile(lambda x: x % 2 == 0, liczby )
    print(list(result))


def itertools_pr6():
    """
    przyklad wykorzystujac iterator dropwhile ktory w tym przypadku zaczyna zapisywac do listy od slowa 
    ktorego dlugosc jest wieksza od 14 i od tego slowa sa pozostale zapisywane slowa niewazne ze nie 
    spelniaja warunku
    """
    north_korea = ["Stalin", "Kim Dzong II", "Kim Ir Sen", "polidbiuro KCPPK", "Pak Hŏn Yŏng", 
            "Kim Tu Bong", "Ch’oe Yong Gŏn"]
    result = dropwhile(lambda x:  len(x) < 14,north_korea )
    print(list(result))

def itertools_pr7():
    """
    przyklad wykorzystujac iterator chain_from_iterable laczy dwie wewnetrzne list tworzac nowa liste
    zawierajace ich wartosc
    """
    anime_winter = [ ["Re:Zero", "Horimiya", "Mushoku Tensei"] , 
            ["Wonder Egg Priority", "Shingeki no Kyojin", "Yuru Camp"] ]
    print("przed ", anime_winter)
    print("po ",list(chain.from_iterable(anime_winter)))

def main():
    print("przyklad 1 wykorzystujacy iterator nieskonczony count()")
    itertools_pr1()
    print("przyklad 2 wykorzystujacy iterator chain()")
    itertools_pr2()
    print("przyklad 3 wykorzystujacy iterator starmap()")
    itertools_pr3()
    print("przyklad 4 wykorzystujacy iterator filterfalse()")
    itertools_pr4()
    print("przyklad 5 wykorzystujacy iterator takewhile()")
    itertools_pr5()
    print("przyklad 6 wykorzystujacy iterator dropwhile()")
    itertools_pr6()
    print("przyklad 7 wykorzystujacy iterator chain_from_iterable()")
    itertools_pr7()

main()
