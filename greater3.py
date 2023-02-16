a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
if a>b and a>c:
    print(f"{a} is greater.")
elif b>c and b>a:
    print(f"{b} is greater.")
elif c>b and a<c:
    print(f"{c} is greater.")
