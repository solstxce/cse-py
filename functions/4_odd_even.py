def odd_even(n):
    if n%2==0:
        return f"{n} is even"
    else: return f"{n} is odd"
n=int(input("Enter a number: "))
print(odd_even(n))