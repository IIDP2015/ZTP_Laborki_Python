
plik=open("dane.txt","r")
tablica=[] 
plik.seek(0)

for i in range(10):
	tablica.append(plik.readline())
   
plik.close()


print("Wczytana tablica:", tablica)

for i in range(len(tablica)):
    tablica[i] = int(tablica[i])

print("Tablica po konwersji:", tablica)