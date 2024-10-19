#!/usr/bin/env python3 
"""
utworzylem dynamiczna klase za pomoca type() 
o nazwie Klasa ktora ma dwa atrybuty pato , noe
"""
Klasa = type('Klasa',(), dict(pato=100, noe="paczka"))
klasa = Klasa()
print(klasa.__class__)
print(klasa.pato)
print(klasa.noe)

"""
utworzylem dynamiczna klase za pomoca type() ktora dziedziczy od klasy Klasa i dwa atrybuty
"""
Kaczapi = type('Kaczapi', (Klasa, ), dict(ziobro="zero", sasin="porozumienie"))
kaczp = Kaczapi()
print(kaczp.__class__)
print(kaczp.ziobro)
print(kaczp.sasin)
print(kaczp.pato)
