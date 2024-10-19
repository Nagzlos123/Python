from functools import wraps
import functools
import time

def example1():
    """
    example tworzy dwie funcje my_decorator i say_whee .funkcja my_decorator przyjmuje jako argument
    funkcje say_whee . Wewnatrz funkcje my_decorator znajduje sie funkcja ktora wykonuje funkcje say_whee
    .Funkcja my_decorator zwraca fukcje wrapper
    Dodalem dwie funkcje ktore bedzie wywolywania w funkcji wrapper
    """
    def my_decorator(func, func2, func3):   
        def wrapper():   
            print("Something is happening before the function is called.")   
            func()    
            func2()
            func3()
            print("Something is happening after the function is called.") 
        return wrapper
    def say_whee(): 
        print("Whee!")
    def wyswielt_tekst(): 
        print("test")
    def wyswielt_tekst2(): 
        print("test2")
    say_whee = my_decorator(say_whee, wyswielt_tekst, wyswielt_tekst2)
    say_whee()

def example2():
    """
    example dziala podobnie co example wyzej jedyna roznica jest taka ze example 2 
    jest uproszczony z powodu dodania adnotacji @my_decorator ,ktora umozliwia wywolanie 
    dekorator  my_decorator  przy wywolaniu fukncji say_whee
    Dodalem dwie dodatkowe funkcje 
    """
    def my_decorator(func):  
        def wrapper():  
            print("Something is happening before the function is called.")   
            func()     
            print("Something is happening after the function is called.")    
        return wrapper
    @my_decorator 
    def say_whee():   
        print("Whee!")
    say_whee()

    @my_decorator
    def say_test():   
        print("test!")
    say_test()
    
    @my_decorator
    def say_test2():   
        print("test2!")
    say_test2()

def example3():
    """
    example tworzy dekorator ktorzy przyjmuje dowolno liczbe  argumentow  zdefiniowanych w funckji my_print
    funkcja my_print jest wywolywane dwa razy wewnatrz funkcji wrapper_do_twice . funkcja my_print
    wyswietla wszystkie arugemnty
    Dodalem dodatkowo arugumenty do funkcji my_print i nowa  dekorowana funkcje
    """
    def do_twice(func): 
        def wrapper_do_twice(*args, **kwargs):    
            func(*args, **kwargs)  
            func(*args, **kwargs)    
        return wrapper_do_twice
    @do_twice
    def my_print(text1 ,text2, text3, text4):   
        print("funkcja my_print",text1, text2, text3, text4)
    my_print('test', 'test2', 'text3', 'text4')
    
    @do_twice
    def my_print2():
        print("funkcja my_print2")
    my_print2()
    
def example4():
    """
    example tworzy dekorator my_decorator ktory  zawiera  wbudowany dekorator @wraps ktory przyjmuje 
    funkcje i dekoruje funkcje wraper .Funkcja wraper zwraca wprowadzona funkcje  
    na koncu wyswietla jest nazwa funkcji i jej dokumentacja ,gdyby nie uzyto @wraps to  wyswietlila sie 
    funkcja wraper a nie example . Dodalem dwie dodatkowo funkcje
    """
    def my_decorator(f): 
        @wraps(f)
        def wrapper(*args, **kwds):  
            print('Calling decorated function') 
            return f(*args, **kwds) 
        return wrapper
    @my_decorator
    def example():   
        """Docstring"""  
        print('Called example function')
    example()
    print(example.__name__)
    print(example.__doc__)

    @my_decorator
    def example2():
        """Docstring2"""  
        print('Called example2 function')
    example2()
    print(example2.__name__)
    print(example2.__doc__)

    @my_decorator
    def example3():
        """Docstring3"""  
        print('Called example3 function')
    example3()
    print(example3.__name__)
    print(example3.__doc__)

def example5():
    """
    example jest podobny co example wyzej tylko zamiast zwracac funkcje bezposrednio jak examplezie wyzej
    wykorzystuje do tego celu zmienna value
    Dodalem dodatkowo funkcje
    """
    def my_decorator(func): 
        @wraps(func) 
        def wrapper(*args, **kwds):   
            print('Wywołanie funkcji dekorowanej')    
            value = func(*args, **kwds)     
            print('Koniec wywołania funkcji dekorowanej')   
            return value  
        return wrapper
    @my_decorator
    def example():  
        """Dokumentacja funkcji"""  
        print('Funkcja dekorowana')
    example()
    print(example.__name__)
    print(example.__doc__ , "\n")

    @my_decorator
    def example2():  
        """Dokumentacja funkcji 2"""  
        print('Funkcja dekorowana 2')
    example2()
    print(example2.__name__)
    print(example2.__doc__ ,"\n" )

    @my_decorator
    def example3(w,y):  
        """Dokumentacja funkcji 2"""  
        print('Funkcja dekorowana 3', w,y)
    example3('poku','kolu')
    print(example3.__name__)
    print(example3.__doc__)

def example6():
    """
    example tworzy dekorator timer ktory sluzy do zliczania czasu wykonywania 
    funkcji dekorowanej waste_some_time ktora podnosi do potegi liczby od 0 do 99999 za pomoca 
    list komprahetnych a potem to sumuje ,dodatkowo funkcja waste_some_time przyjmuje parametr ktory okresla 
    ile razy ma wykonywac ta operacje 
    Dodalem dwie funkcje dekerujace .Pierwsza za pomoca wyrazenia lambda podnosi liczby od 0 do 99999 do 
    kwadratu a za pomoca kolejnego wyrazenia lambda sumuje je.Druga wyszukuje liczby parzyste z zakresu
    od 0 do 999
    """
    def timer(func):  
        """Print the runtime of the decorated function"""    
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):   
            start_time = time.perf_counter()       
            value = func(*args, **kwargs)   
            end_time = time.perf_counter()      
            run_time = end_time - start_time      
            print("Finished  {0} in {1:.4f} secs".format(repr(func.__name__) ,run_time ))      
            return value 
        return wrapper_timer
    @timer
    def waste_some_time(num_times):   
        for _ in range(num_times):  
            sum([i**2 for i in range(10000)])
    waste_some_time(5)

    @timer
    def funkcja_sumowanie():
        functools.reduce(lambda z,y: z + y ,map(lambda x: x*x , range(100000)))
    funkcja_sumowanie()

    @timer
    def funkcja_parzyste():
        [i for i in range(1000) if i % 2 == 0]
    funkcja_parzyste()

def example7():
    """
    example tworzy klase Person ktora ma metody fget ,fset i fdel.Metoda fget wyswietla i zwraca przypisana
    wartosc do wlasciwosc name. Metoda fset odpowiada ze ustawiania wartosc atrybutowi name. Metoda fdel
    odpowiada za usuwanie  zmiennej name ,nastepnie wykorzystujac funkcje property jest tworzony deskryptor 
    Dodalem obslugue wyjatkow w metodach fget i fdel i sprawdzanie wartosc przypisywanych do name czy sa typu
    string
    """
    class Person(object):   
        def init(self): 
            self._name = ''    
        def fget(self):  
            try: 
                print ("Getting: %s" % self._name  ) 
                return self._name
            except:
                print("nie zadeklarowano name")
        def fset(self, value):
            if(isinstance(value, str)):
                print ("Setting: %s" % value) 
                self._name = value.title() 
            else:
                raise ValueError("niewlasciwy typ") 
        def fdel(self): 
            print ("Deleting: %s" %self._name)  
            try:
                del self._name 
            except:
                print("nie zadeklarowano name")
        
        name = property(fget, fset, fdel, "I'm the property.")
    user = Person()
    user.name = 'john smith'
    print(user.name)
    del user.name
    user.name = 'janusz korwin'
    print(user.name)
    user.name = 'janusz bobola'
    del user.name

def example8():
    """
    example tworzy metode ktore beda odpowiadac za usuwanie zmiennej , wyswietlanie zawartosc 
    zmiennej i przypisywania wartosc zmiennej . Wykorzystujac funkcje property tworzy deskryptor klasy .
    Konstruktor klasy Alphabet przyjmuje wartosc ktora zostanie przypisana do zmiennnej value
    Dodalem  obsluge wyjatkow w metodach getValue ,  DelValue i   sprawdzanie czy wartosc ktora ma byc 
    przypisana do zmiennej ma odpowiednia dlugosc
    """
    # Alphabet class 
    class Alphabet: 
        def __init__(self, value):   
            self._value = value 
        # getting the values 
        def getValue(self):  
            try:
                print('Getting value')   
                return self._value   
            except:
                print("zmienna nie jest zadeklarowana")
        # setting the values 
        def setValue(self, value):   
            if(len(value) < 10):
                print('Setting value to ' + value)     
                self._value = value
            else:
                raise ValueError("nie udalo sie przypisac wartosc do zmiennej poniewaz przekraczana", 
                        "ona  wyznaczono dlugosc") 
        # deleting the values
        def delValue(self):   
            try:
                print('Deleting value')    
                del self._value
            except:
                print("zmienna nie jest zadeklarowana")
        value = property(getValue, setValue, delValue, ) 
    # passing the value
    x = Alphabet('GeeksforGeeks') 
    print(x.value) 
    x.value = 'GfG'
    del x.value
    x.value = 'WWW'
    print(x.value) 
    x.value = 'asX'

def example9():
    """
    example tworzy deskryptor wykorzystujac  dekarator property dodatkowa w klasie Person znajduja sie 
    dekorator .setter i deleter. Setter wskazuje  na metode ktora ustawiania wlasciwosc name a deleter 
    wskazuje na metoda ktore jest odpowiedzialna za usuwania wlasciwosc name
    Dodalem obsluge wyjatkow 
    """
    class Person(object):  
        def init(self):   
            self._name = '' 
        @property  
        def name(self):  
            try:
                print("Getting: %s" % self._name)  
                return self._name
            except:
                print("zmienna name nie jest zadeklarowana")
        @name.setter 
        def name(self, value):  
            print ("Setting: %s" % value )
            self._name = value.title()    
        # deleting the values  
        @name.deleter 
        def name(self): 
            try:
                print ("Deleting: %s" % self._name)   
                del self._name
            except:
                print("zmienna name nie jest zadeklarowana")

    user = Person()
    user.name = 'john smith'
    print(user.name)
    del user.name
    user.name = 'osama baraka'


def example10():
    """
    example tworzy deskryptor wykorzystujac  dekarator property dodatkowa w klasie Alphabet znajduja sie 
    dekorator .setter i deleter. Setter wskazuje  na metode ktora ustawiania wlasciwosc value a deleter 
    wskazuje na metoda ktore jest odpowiedzialna za usuwania wlasciwosc value. Klasa przyjmuje w 
    konstruktorze jeden parametr ktory przypisuje wartosc poczatkowa wlaciwosc value
    Dodalem obsluge wyjatkow
    """
    class Alphabet: 
        def __init__(self, value):   
            self._value = value   
        # getting the values   
        @property 
        def value(self): 
            try:
                print('Getting value')  
                return self._value 
            except:
                print("zmienna value nie jest zadeklarowana")
        # setting the values        
        @value.setter  
        def value(self, value):   
            print('Setting value to ' + value)  
            self._value = value  
        # deleting the values  
        @value.deleter
        def value(self):  
            try:
                print('Deleting value') 
                del self._value
            except:
                print("zmienna value nie jest zadeklarowana")
    # passing the value
    x = Alphabet('Peter')
    print(x.value)
    x.value = 'Diesel'
    del x.value
    x.value = 'Gaz'

def main():
    print("example 1")
    example1()
    print("\nexample 2")
    example2()
    print("\nexample 3")
    example3()
    print("\nexample 4")
    example4()
    print("\nexample 5")
    example5()
    print("\nexample 6")
    example6()
    print("\nexample 7")
    example7()
    print("\nexample 8")
    example8()
    print("\nexample 9")
    example9()
    print("\nexample 10")
    example10()
main()
