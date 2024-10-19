#!/usr/bin/env python3
def ex_1():
    """funkcja wyswietla  w postaci listy  wartosc podniesione do kwadratu listy o nazwie x """
    square = lambda x : x * x
    x = [1, 2, 3, 4, 5]
    print("ex1 = ",list(map(square, x)))

def ex_2():
    """funkcja robi to samo co  funkcja ex_1 ale teraz zamiast wykorzystywac lambe wykorzystujemy funkcje  """
    x = [1, 2, 3, 4, 5]
    def square(num):
        return num * num
    print("ex2 = ",list(map(square,x)))

def ex_3():
    """ robi to samo co funkcja ex_1  jedyna roznica jest ze w ex_1 jest tworzonoi zmienna square  ktore 
    przechowuje  wyrazanie lambda """
    x = [1, 2, 3, 4, 5]
    print("ex3 = ",list(map(lambda num: num * num, x)))

def ex_4():
    """dzialanie przykladu jest takie  ze do zmiennej sa przypiswane  wyniki  mnozanie obecnej wartosc  zmiennej 
    product z zmienna  num"""
    product = 1
    x = [1, 2, 3, 4, 5]
    for num in x:
        product = product * num #kolejne iteraje  1 , 2 , 6, 24 , 120 
    print("ex4 = ",product)

def ex_5(): 
    """ ma takie same dzialanie jak przyklad 4 ale  zamiast zwyklej petli wykorzystuje   funckje reduce wraz
    z wyrazeniem lambda na poczatku 1 * 2 wynik tego jest nastepnie jest   mnozony przez koljene liczbe na
    liscie i tak dalej az lista sie skonczy
    """   
    from functools import reduce
    product = reduce((lambda x, y: x*y), [1, 2, 3, 4])
    print("ex5 = ",product)

def ex_6():
    """
     wyrazenie lambda  sprawdza czy a jest wieksze od b  jesli a jest wieksze zwraca a jesli b to b
     najwieksze liczba zostaje a zamieniana jest mniejsza 
     i tak dopuki nie znajdzie najwiekszej wartosc w liscie 
    """
    from functools import reduce
    lis = [1, 3, 5, 6, 2]
    output = reduce(lambda a,b : a if a > b else b ,lis)
    print("ex6 = ",output)

def ex_7():
    """
    na poczatku  do zmiennej  x jest przypisywana  wartosc od -5 do 5  
    nastepnie jest tworzona nowa pusta lista
    nastepnie w petli sa sprawdzane czy wartosc przypisane do x sa mniejsze od 0 jesli tak sa 
    przypisywane do wczesniej utworzonej listy
    """
    x = range(-5,5)
    new_list = []
    for num in x:
        if num < 0:
            new_list.append(num)
    print("ex7 = ",new_list)
    
def ex_8():
    """
    do zmienej x sa przyspisywane wartosc od - 5 do 5
    nastepnie w zmiennej  all_less_than_zero jest zapisywane w postaci list  wyniki metody
    filter w której znajduje sie  wyrazenie ktora sprawdza czy wartosc sa mniejsze od 0 jesli tak to 
    przypisuje je do listy
    """
    x = range(-5, 5)
    all_less_than_zero = list(filter(lambda num: num < 0, x))
    print("ex8 = ",all_less_than_zero)

def ex_9():
    """
    przyklad  na poczatku tworzy dwa tuple a i b 
    nastepnie  tworzy zmienna x do ktorej jest zapisywane  zwrocoy obiekt zip (tuple) ,  
    który jest polaczeniem  tuple a i b
    na koncu jest wyswietlana zawartosc zmiennej x 
    """
    a = ("John", "Charles",  "Mike" )
    b = ("Jenny", "Christy", "Monica", "Vicky")
    x = zip(a,b)
    print("ex_9 = ",*x) #('John', 'Jenny') ('Charles', 'Christy') ('Mike', 'Monica')

def ex_10():
    """
    na poczatku sa imporowane moduly  functools i operator
    nastepnie wykorzystuja reduce wyswietlane jest wynik  calkowite sumy elementow zawarty w przekazanej
    liscie  funckja sum robia to samo co wynijka wyzej
    """
    import functools, operator
    w1 = functools.reduce(operator.add, [1 ,2, 3, 4], 0 ) #10
    sum([1, 2, 3, 4]) #10
    print("ex10 = ",w1)

def ex_11():
    """
    importowany jest modul functools
    tworzono jest zmienna product
    nastepnie  petla iteruje po liscie
    w czasie dzialanie petli kolejnych iteracjach petli przypisywane sa kolejne wynik mnozenia wartosc 
    zmniennej product i i 
    """
    import functools
    product = 1
    for i in [1, 2, 3]:
        product *= i  #6
    print("ex11 = ",product)

def ex_12():
    """
    wynik bedzie taki sam jak w przykladzie ex_11  tylko ze wszystko jest wykonywane w jednej
    linijce  wykorzystuja funkcje reduce i operator mnozenie ktory bedzie mnozyl kolejne elementy  listy
    na koncu zwroci koncowy wynik mnozenia 
    """
    import functools,operator
    product = functools.reduce(operator.mul, [1,2,3],1) # 6
    print("ex12 = ",product)

if __name__ == '__main__':
    ex_1()
    ex_2()
    ex_3()
    ex_4()
    ex_4()
    ex_5()
    ex_6()
    ex_7()
    ex_8()
    ex_9()
    ex_9()
    ex_10()
    ex_11()
    ex_12()
