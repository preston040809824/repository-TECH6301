n=int(input("Enter the value for 'N': "))
a=0
b=1
c=0

print(a)
print (b)

while n>0:
    c=a+b
    a=b
    b=c
    n=n-1
    print(c)
