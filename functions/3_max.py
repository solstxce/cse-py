def maxi(a,b,c):
    if a>b and a>c:
        return a
    else:
        if b>c:
            return b
        else:
            return c
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
print("Maxmium of 3 numbers is:",maxi(a,b,c))