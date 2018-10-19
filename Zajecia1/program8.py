
try:
	plik=open("dane.txt","w")
	for i in range(10):
		plik.write(str(i) + "\n")
    
except IOError:
	pass
finally:
	plik.close()