class A(object):
    def metodaX(self):
        print ("# A.metodaX")
        return "Ala"
 
class B(A):
    def metodaX(self):
        print ("# B.metodaX")
        return super(B, self).metodaX() + " ma"
 
class C(B):
    def metodaX(self):
        print ("# C.metodaX")
        return super(C, self).metodaX() + " kota."
 
    def metodaY(self):
        print ("# C.metodaY")
        return super(C, self).metodaX() + " psa."
 
x = C()
print(x.metodaX())
print(x.metodaY())
print(super(C, x).metodaX())
print(super(B, x).metodaX())