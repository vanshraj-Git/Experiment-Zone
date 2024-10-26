a=[1,"me",2,"himmat",2,"henry"]
print(type(a))
print(a[5])
print(a)

if 2 in a:
    print("yes")
else:
    print("no")
if 'mat' in 'himmat':
    print("yes")
else:
    print('no')


z=[i for i in range(5) if i%2==0]
print(z)
print(type(z))
z=[i for i in range(5)]
print(z)
names=["milo","sarah","kaido","rose"]
nameswith_o=[j for j in names if "o" in j]
print(nameswith_o)
