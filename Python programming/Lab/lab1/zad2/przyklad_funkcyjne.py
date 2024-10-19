#!/usr/bin/env python3

#przyklad 1
def ex_1():
    """
        przyklad podwaje kazdy element z listy  wykorzystuje przytym wyrazenie lambda zawarte w zminnej
        divide
    """
    divide = lambda y: y  + y
    y = [1, 4, 9, 16, 25]
    print("przyklad 1 " ,list(map(divide , y)))

#przyklad 2
def ex_2():
    """
        przyklad podwaje kazdy element z listy  wykorzystuje przytym wewnatrzna funkcje  sum_1 która 
        zwraca podwoja wartosc
    """
    x = [3, 2 ,1 ,5, 7]
    def sum_1(number):
        return number + number
    print(x, "przyklad 2", list(map(sum_1, x)))
    
# przyklad 3
def ex_3():
    """
        przyklad wykonuje konkatenacje tego samego elementu wykorzystuja 
        wyrazenia lambda wraz z funkcja map ktora znajduje w print() 
    """
    z = ["ad", "as", "xx1", "a", "xx"]
    print( z , "przyklad 3",  list(map(lambda st: st + st , z )))

#przyklad 4
def ex_4():
    """
     przyklad wykonuje  odejmowanie  od zmiennej start liczby zawarte w 
     liscie wykorzystuje przy tym petla ktora iteruje]
     po liscie 
    """
    start = 33
    liczby = [3,2,5,6,7]
    for num in liczby:
        start = start - num
    print( "przyklad 4 ", start )

# przyklad 5
def ex_5():
    """
    przyklad wykonuje  odejmowanie  zawartosc  pierwszego elementu przez  pozostale elementy listy
    wykorzystuje przy tym wyrazenie lambda wraz z funkcja reduce zwraca ten sam wynik co przyklad 4
    """
    from functools import reduce
    wynik_odejmowania = reduce((lambda w, z: w - z ), [33,3, 2, 5, 6, 7])
    print("przyklad 5 ",wynik_odejmowania)

# przyklad 6 
def ex_6():
    """
    przyklad  zwraca najdluzszy string  z listy slowa
    """
    from functools import reduce
    slowa = ["wawa", "janek","aa","miroslaw", "karowaka", "Kawaii","panstwopolin2s"]
    naj = reduce(lambda sl1,sl2 : sl1 if len(sl1) > len(sl2) else sl2, slowa )
    print("przyklad 6 ",naj)

# przyklad 7
def ex_7():
    """
        przyklad tworzy nowa liste new_words a nastepnie przypisuje do niej slowa (znajdujace
        sie w tuple x )  ktorych dlugosc jestmniejsza od 3 
    """
    x = ("was", "the", "super", "towar" , "hl")
    new_words = []
    for word in x:
        if len(word) < 3:
            new_words.append(word)
    print("przyklad 7" , new_words)

#przyklad 8
def ex_8():
    """
    tworzy liste  ktora zawiera elementy o dlugosc wiekszej od 2 za pomoca  wyrazenia lambda i  funkcji
    filter()
    """
    w1 = ["wak", "sa", "ssa","a"]
    all_word = list(filter(lambda w: len(w) > 2, w1))
    print("przyklad 8 ",all_word)

#przyklad 9 
def ex_9():
    """
        przyklady laczy trzy listy w jedna 
    """
    nptv = ["Marcin", "Radoslaw", "Aleksander" , "Maciej"]
    nptv_naz = ["Osadowski", "Siedlecki", "Jablonowski"]
    nick=["Ludwiczek","Radzio", "Jasczur"]
    lista_osob = list(zip(nptv,nptv_naz, nick))
    print("przyklad 9 ",lista_osob)

#przyklad 10 
def ex_10():
    """
        przyklady dokleja do ciag "ss" kolejne elemnty listy wykorzystujac przytym  operator add i funkcje 
        reduce ktora zwraca  zlaczony ciag 
    """
    import functools, operator
    print("przyklad 10 ",functools.reduce(operator.add, ["aa", "dd", "aa", "as"],"ss"))

#przyklad 11
def ex_11():
    """
        przyklad dodaje kolejne elementy  listy do zmiennej dod 
    """
    import functools
    dod = 240
    for i in [1, 4, 5]:
        dod += i 
    print("pryklad 11", dod)

#przyklad 12
def ex_12():
    """
        przyklad dodaje do liczby koljene elementy listy i  odejmuje kolejene elementy listy 
        wykorzystuje przy tym operatro add i sub i funkcje reduce()
    """
    import functools, operator 
    add = functools.reduce(operator.add , [1,2,3,5,6],1)
    odd = functools.reduce(operator.sub, [2,3,5],200)
    print( "przyklad 12 ", add , odd )

def main():
    ex_1()
    ex_2()
    ex_3()
    ex_4()
    ex_5()
    ex_6()
    ex_7()
    ex_8()
    ex_9()
    ex_10()
    ex_11()
    ex_12()
main()
