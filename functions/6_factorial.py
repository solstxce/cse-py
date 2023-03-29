def fact(n):
    f=1
    while n>0:
        f*=n
        n-=1
    print(f"Factorial of {n}: {f}")
fact(int(input("Enter a number: ")))
