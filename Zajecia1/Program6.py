
import string

def zlicz_znaki(tekst, litery=string.ascii_letters):
    litery=frozenset(litery)
    licznik=0
    for znak in tekst:
        if znak in litery:
            licznik+=1
    return licznik

print("",zlicz_znaki("informatyka"))
print("",zlicz_znaki("ma"))
