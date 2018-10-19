#Instrukcja warunkowa if

x = int(input('Podaj wartość x: '))
if x:
    print("x jest niezerowe")
if x<10:
    print("wartość jednostkowa!")
elif x<100:
    print("wartość rzędu dzieisiątek!")
elif x<1000:
    print("wartość rzędu setek!")
else:
    print("Wartość co najmniej rzędu tysiąc!")
