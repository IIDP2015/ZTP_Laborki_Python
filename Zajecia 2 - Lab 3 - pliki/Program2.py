import Program1

a=Program1.Point()
print(repr(a))

b=Program1.Point(5,8)
print(str(b))

print(b.distance_from_origin())

b.x=-19

print(str(b))

print(a==b, a!=b)
