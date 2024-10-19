#!/usr/bin/env python3
"""
przyklad 1  tworzy dekorator z parametrem i funkcje dekorujaca ktora dzieli paremetry a i b
"""
def example(funkcja):
    def wrapper(*args, **kwargs):
        print("Poczatek wywolaniem funkcji example")
        funkcja(*args, **kwargs)
        print("Po wywolanie funkcji")
    return wrapper
@example
def dziel(a, b):
    print("wynik = ",a / b)

"""
przyklad 2 tworzy dekarotor z parametrem i 
funkcja dekerowana ktora ma za zadania wymnazac wszystkie  podane parametry 
"""
def example2(funkcja):
    def wrapper(*args, **kwargs):
        print("Poczatek wywolaniem funkcji example2")
        funkcja(*args, **kwargs)
        print("Po wywolanie funkcji")
    return wrapper
@example2
def wymnoz(a, b, c, d , e, f):
    print ("To jest zwykła funkcja, która dodaje liczby:")
    print ("wynik = ",a * b *c *d * e * f)

def main():
    print("przyklad 1")
    dziel(22,2)
    print("\nprzyklad 2")
    wymnoz(1,2,3,4,5,6)
main()
