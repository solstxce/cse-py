a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
operator=input("Enter operator: ")
if operator=="is":
    result=(a is b)
elif operator=="is not":
    result=(a is not b)
print(f"Test case is 'a {operator} b'.")

print(f"The result is {result}.")
