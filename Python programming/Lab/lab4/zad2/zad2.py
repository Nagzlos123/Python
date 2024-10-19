#!/usr/bin/env python3
class Pusta:
    pass
pusta = Pusta()
print(dir(pusta))
"""
Ta metoda zwraca rozmiar obiektu
"""
print("metoda __sizeof__() " ,pusta.__sizeof__())
"""
Ta metoda jest wywoływana, gdy funkcja print () lub str () jest wywoływana na obiekcie.
Ta metoda zwracać obiekt String. Jeśli nie zaimplementujemy funkcji __str __ () dla klasy, wtedy
używana jest wbudowana implementacja obiektu, która faktycznie wywołuje funkcję __repr __ (). 
"""
print("metoda __str__() ",pusta.__str__())
"""
zwraca reprezentację obiektu w formacie łańcucha.i
Ta metoda jest wywoływana, gdy funkcja repr () jest wywoływana na obiekcie.
"""
print("metoda __repr__()", pusta.__repr__())
"""
zwraca wszystkie zdefiniowa atrybut w postaci slownika (atrybut:wartosc)
"""
pusta.c = 5
print("atrybut __dict__ ",pusta.__dict__)
"""
__delattr__() - usuwa atrybut
__setattr__() - ustawia atrybut
"""
