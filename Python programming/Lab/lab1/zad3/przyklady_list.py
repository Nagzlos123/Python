#!/usr/bin/env python3
from matplotlib import pylab
from pylab import * 

def ex1():
    """
    przyklad podwaja wartosc elementow listy
    """
    print([x + x for x in [22,33,44,11,5,6]])

def ex2():
    """
        przyklad na dwa sposoby  wybiera elementy o dlugosc wiekszej niz 
        2 z listy
    """
    word = ["as","aaa","a","dsds","as2","aw"]
    print("za pomoca programowania funk : ",(list(filter(lambda chr1:  len(chr1) > 2,word ))))
    print("za pomoca list komprahetnych: ",[x for x in word if len(x) > 2 ])

def ex3():
    """
    pryklad   tworzy zagnizezdzona liste skladajace sie z kilku krotek  .Krotki sa genrowanie w zaleznosc 
    od liczby x ktore musze byc wieksze od 0  i y ktore musza byc mniejsze od 8 .
    Wartosc x i y tworza tyle  tupli ile  wynosi wartosc wyrazenia
    liczby  x  *  liczby y  (ktore spelnily warunek) 
    """
    w = [ (x,y) for (y,x) in [(y,x) for y in range(11) for x in range(4) if x > 0 and y < 8]]
    print(w)
        

def ex4():
    """
    przyklad tworzy dwie talicy jedna pusta a druga jest lista zagnizezdzona skladajace sie z jednej listy 
    ktora ma dwie listy
    za pomoca petli dwie wewnetrzne listy sa dzielone na cztery wewnetrzne listy
    """
    now_tab = []
    mat_sl  = [['W', 'A', 'R', 'S'],[ 'Z', 'A', 'W', 'A']]
    for i in range(len(mat_sl[0])):
        transposed_now = []
        for row in mat_sl:
            transposed_now.append(row[i])
        now_tab.append(transposed_now)
    print(now_tab)

def ex5():
    """
    przyklad tworzy  zagniezdza liste pierwsze list pierwsza lista posieda 4 elementy ktore stanowia listy 
    dwuelementowe 
    nastepnie za pomoca isty comprehentnej na poczatku laczy elementy list ktore sa o indeksie 0 tworzac nowa
    liste to samo robi z elementami o indeksie 1 potem z tak utworzonej listy tworzy liste ktora zawiera
    elementy dwoch poprzednio stworzonych list
    Na koncu jest wyswietlana utworzona lista 
    """
    matrix = [ ['W', 'Z'], ['A', 'A'], ['R', 'W' ], ['S', 'A'] ]
    print("przed: " ,matrix)
    w1 = [ num for row in  [ [ row[x]  for row in matrix ] for x in range(2)  ]for num in row]
    print("po: ",w1)

def ex6():
    """
    program tworzy  liste slow a nastepnie wybiera z niej slowa wieksze od 4
    potem wykonuje  konkatenacje tego samego elementu tyle razy  ile uzytkownik wpisał przy starcie programu  
    """
    ilosc = int(input("Podaj ile razy  bedzie konktatenowany  ten sam element  "))
    word = ["dsadsad", "dsadas","sssa","aaadsdad"]
    sl_wieksze = list(map (lambda word:  word * ilosc  , list(filter (lambda word:  len(word) > 4 , word 
        )))) 
    print("przed : ",word)
    print("po:" ,sl_wieksze)

def ex7():
    """
    program tworzy liste slow a nastepnie wybiera slowa dluzsze od 2 a na koncu podwaje  uzyskane
    slowa 
    """
    w = ["sss","aaa","as","adsd","aasw","awawa"]
    print("przed: ",w)
    slowa_wieksze = [chr1 + chr1 for chr1 in w if len(chr1) > 3 ]
    print(slowa_wieksze)

def ex8():
    """
    przyklad na poczatku tworzy liste z wartosc od 1 do 19 nastepnie sprawdza czy elementy maja wartosc 
    mniejsza od 15 a na koncu sprawdza czy wartosc  listy sa wikesze od 5 jesli tak to podniosiu je
    do kwadratu jesli nie podwaje je  
    """
    print([(x * x  if x > 5  else  x + x) for x in [x for x in range(20)]  if x < 15])

def ex9():
    """
    przyklad na poczatku tworzy liste 
    potem ja wyswietla 
    a na koncu jej zawartosc jest  wyswietlna duzymi literami na dwa sposoby 
    """
    slowa = [ "sawa", "awawa", "kawaka", "Nowak", "Senpai" ]
    print("przed: ",slowa)
    print("1 sposob: ",([ i.upper()  for i in slowa  ]))
    print("2 sposob: ", [i[0].upper() + i[1:].upper()  for i in slowa])

def ex10():
    """
    program tworzy zagniezdzana liste ktora ma 6 list dwuelementowyw  wewnatrz.
    Nastepenie ta lista jest przeksztalcona na slownik z ktorego potem  sa wybierane osoby ktorzy 
    pracuja jako  infromatyk i wypisuje ich stanowiska duzymi literami .Na koncu jest wyswietla ilosc 
    pracownikow na tym stanowisko wraz z osobami na tym stanowisku 
    """
    firma_stanowiska = [
        ['Michal','mechanik'],
        ['Rafal','mechanik'],
        ['Kasia','kurier'],
        ['Miroslaw','informatyk'],
        ['Grzegorz','informatyk'],
        ['Arek','sekretarz']
    ]
    slownik_osob = {osob: st for osob,st in firma_stanowiska}
    print("wszystkie osoby wraz ze stanowiskami : ",slownik_osob)
    inf = {osob: st.upper() for osob, st in slownik_osob.items() if st == "informatyk"}
    print("tylko informatycy ",inf)
    print("infromatycy ", [osob for osob in inf.keys()] )
    print("liczba informatykow ", len(inf))

def ex11():
    """
    program ma za zadanie zapisac do slownika liczby od 1-9 jako klucz ,a wartosc maja byc podnoszone do 
    kwadratu jesli liczba jest nieparzysta ,a podwoja   jesli liczba jest parzysta. Progra ten jest 
    realizowanny na dwa sposoby . Pieerwszy sposob jest standardowy ykorzystujac petle for i instrukcje 
    warunkowe . Drugi o wiele krotszy wykorzystuje listy comprahetne
    """
    slownik_dict = dict()
    for licz in range(1,10):
        if licz % 2:
            slownik_dict[licz] = licz  * licz 
        else:
            slownik_dict[licz] = licz + licz 
    print("wykorzystujac standardowe metode ",slownik_dict)
    print ("wykorzystujac listy compraetne: " , {licz: licz * licz if licz % 2 else licz + licz for licz in range(1,10) })

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
