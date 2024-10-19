#!/usr/bin/env python3 
def pr1_gen():
    """
    przyklad za pomoca wyrazenia generatowego wypisuje dlugosc kazdego elemnetu tupli re_zero_characters    
    umieszczajac je w tuplie
    """
    re_zero_characters = ("Ram", "Emilia", "Subaru", "Nekopara", "Beatrice", "Puck")
    gen = (len(w) for w in re_zero_characters)
    print(tuple(gen))

def pr2_gen():
    """
    przyklad za pomoca wyrazenia generatorowego zamienia liczby zawarte w liscie na znaki  
    """
    liczba = [88,33,22,66,78,88]
    print (list(chr(l) for l in liczba))

def pr3_gen():
    """
    przyklad za pomoca wyrazenia generatorowego wypisuje  slowo ktora sa dluzsze niz 4 zapisujac je w tupli 
    """
    liczba = ("Rita", "Soa", "Rie Takarisha")
    print(tuple(x for x in liczba if len(x) > 4))

def main():
    print("przyklad 1 wyrazenia generatorowego bez funkcji ")
    pr1_gen()
    print("przyklad 2 wyrazenia generatorowego bez funkcji ")
    pr2_gen()
    print("przyklad 3 wyrazenia generatorowego bez funkcji ")
    pr3_gen()

main()
