
def dodaj_jesli_parzysta(x, lista=None):
    if lista is None:
        lista=[]
    if x%2==0:
        lista.append(x)
    return lista


print(dodaj_jesli_parzysta(2))
print(dodaj_jesli_parzysta(5,[4,6,7,8]))
print(dodaj_jesli_parzysta(10,[4,6,7,8]))
