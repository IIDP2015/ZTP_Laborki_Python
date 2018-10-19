
tablica=[1,4,6,3,2,1,8]

import pickle

plik=open("tablica.txt","wb")
pickle.dump(tablica,plik)
plik.close()


plik=open("tablica.txt","rb")
tablica2 = pickle.load(plik)
plik.close()
print('Tablica po "odpicklowaniu":', tablica2)

