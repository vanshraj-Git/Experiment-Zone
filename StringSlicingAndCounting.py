a=" my name is vanshraj."
count=0
#  0123456789012345678
# shift+O run code
print(a[12:17])
print(a[0:20]) or print(a[0:-1]) or print(a[::1]) or print(a[0:-1])
print(a[-1:-20]) or print(a[19:0:-1]) or print(a[::-1])
for i in a:
    count=count+1
    if(i=="."):
        break
    print("Total no. of indexes in string: "+ i)
print(count)        
