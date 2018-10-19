
s= input("Podaj liczbę całkowitą dziesiętną: ")
try:
    i=int(s)
    print("Podano prawidłową liczbę całkowitą, która wynosi: ",i)
except ValueError as err:
    print(err)
