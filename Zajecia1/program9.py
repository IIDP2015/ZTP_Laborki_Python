plik=open('dane.txt','rt')
try:
  print(plik.read())
except IOError:
  pass
finally:
  plik.close()