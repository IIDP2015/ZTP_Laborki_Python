#budowa funkcji

import math

def heron(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Pole trójkąta o bokach 2,4,5 wynosi:",heron(2,4,5))
