#!/usr/bin/env python3 
from functools import wraps
"""
Roznica pomiedzy  przyklad1 a przykladem2 jest taka ze jeden uzywa @wraps a drugi tego nie uzywa
.Dekorator @wraps umozliwia w instrukcjach example.__name__ i example.__doc__ 
wyswietlenie ze wywolano funkcje example i  dokumnetacja dotyczaca funkcji example() zamiast funkcji wrapper()
"""
def przyklad1():
    def my_decorator(f):  
        def wrapper(*args, **kwds):
            """Wraper doscstring"""
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

def przyklad2():
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

def main():
    print("bez uzycia dekoratora wraps")
    przyklad1()
    print("\nz uzyciem dekoratora wraps")
    przyklad2()

main()
