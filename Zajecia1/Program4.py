

#instrukcja sterująca while

print("Podaj liczby całkowite, po każdej naciśnij Enter:")

total=0
count=0

while True:
    line=input("liczba całkowita: ")
    if line:
        try:
            number=int(line)
        except ValueError as err:
            print(err)
            continue
        total+=number
        count+=1
    else:
        break

import math

if count:
    print("ilość=", count,", suma=",total,", średnia=",total/count,", pierwiastek z sumy liczb=",math.sqrt(total))
