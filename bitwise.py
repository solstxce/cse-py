a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
operator=input("Enter operator: ")
if operator=="&":
    result=a&b
elif operator=="|":
    result=a|b
elif operator=="^":
    result=a^b
elif operator=="~":
    result=~(a|b)

print(f"{a} {operator} {b} is {result}")
