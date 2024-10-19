#!/bin/env python3
from functools import reduce

def pod1_funkcyjne(list1):
   """
    program wykorzystujac programowanie funkcyjne wyszukuje liczby ktore  sa nieparzyste z zakresu listy 
    ,ktorej zakres  definiuje  uzytkownik podczas uruchamiana .
    list jest przekazywana z pomoca parametru funkcji
   """
   return (reduce(lambda x,y: x +y,(list(filter(lambda x:  x % 2 ,
        list1[int(input("Zakres poczatek ")):int(input("zakres koniec "))] )))))

def pod1_listy(list1):
    """
    program robi to samo co  program wyzej tylko wykorzystuje zamiast programowania funkcyjnego
    listy comprahetne
    """
    return(sum([ x for x in list1[int(input("Zakres poczatek ")):int(input("zakres koniec "))] if x % 2]))

def pod3_funkcyjne(slowo, zn):
    """
    program ma za zadanie  wyswietlic ile dane slowo pojawilo sie w tekscie 
    w tym celu wykorzystalem programowanie funkcyjne  w tym  funkcje filter i wyrazenia lambdy
    .Slowo ktorego  ilosc pojawien jest liczona jest wprowadzane  przez uzytkownika .
    Slowo i tekst sa to argument funkcji
    """
    return(len(list(filter(lambda x: x == zn  ,slowo))))

def pod3_listy(slowo,xz):
    """
    program robi to samo co program wyzej tylko wykorzystuje przy tym listy comprahetne
    """
    return(len([zn for zn in slowo if zn == xz ]))

def pod2_funkcyjne():
     """
        program ma za zadanie liczenie sumy  elementow listy ktorych wartosc nie sa wieksze od zakresu
        podanego przez uzytkownika  . W programie wykorzystuje  w tym celu programowanie  funkcyjne
     """
     zakres = int(input("podaj liczbe do ktrej bedzie liczono suma " ))
     return (reduce(lambda x,y: x + y,(list(filter(lambda x: x <=  zakres ,[2,4,5,1,9,2,33,22,3] )))))

def pod2_listy():
    """
    program robi to samo co wyzej tylko wykorzystuje do tego listy comprahetne
    """
    zakres = int(input("podaj liczbe do ktrej bedzie liczono suma " ))
    return (sum([num for num in [2,4,5,1,9,2,33,22,3] if num <= zakres ]))

def pod4_funkcyjne():
    """
    
    """
    test = []
    s = 1
    faktura = [[10,3,0.02], [22, 10, 0.05], [7, 8, 0.03] ]
    for x in range(len(faktura)):
        for w in faktura[x]:
            if w < 1.00:
                w = 1.00 - w
            s *= w     
            print(w)
        test.append(s)
    print()

def pod4_listy():
    """

    """
    faktura = [[10,3,0.02], [22, 10, 0.05], [7, 8, 0.03] ]

if __name__ == '__main__':
    list1 = [1,2,3,4,5,7,8,9,10]
    #print("Podpunkt  1 wykonany za pomoca programowanie funkcyjnego ",pod1_funkcyjne(list1))
    #print("Podpunkt  1 wykonany za pomoca List Comprehensions  ",pod1_listy(list1))
    tekst = """hi i am new to the pentesting world and i have been learning recently how to 
    capture wifi handshakes and cracking them with aircrack ng. but i have recently learned that there is 
    hashcat which is a lot faster than aircrack ng"""
    #print("Podpunkt  3 wykonany za pomoca programowanie funkcyjnego",
      #      pod3_funkcyjne(tekst.split(), input("Podaj wyraz ")))
    #print("Podpunkt  3 wykonany za pomoca List Comprehensions" ,
      #      pod3_listy(tekst.split(), input("Podaj wyraz")))
    #print("Podpunkt  2 wykonany za pomoca programowanie funkcyjnego ",pod2_funkcyjne())
    #print("Podpunkt  2 wykonany za pomoca List Comprehensions " ,pod2_listy())
    pod4_funkcyjne()
    pod4_listy()
