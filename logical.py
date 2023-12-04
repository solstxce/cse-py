a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
print(a)
print(b)
operator=input("Enter operator: ")
if operator=="and":
    result=(a<b and a<b*2)
elif operator=="or":
    result=(a<b or a<b*2)
if operator=="not":
    result=not(a<b and a<b*2)
print(f"The test case is 'a < b {operator} a < b*2' ")
print(f"The result is {result}.")
