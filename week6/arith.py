def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def prod(a,b):
    return a*b
def div(a,b):
    return a/b
def calculate(operation,a,b):
    return operation(a,b)
a=int(input("Enter 1st num: "))
b=int(input("Enter second num: "))
o=input("Enter operation: ")
if o=="+": res=calculate(add,a,b)
elif o=="-": res=calculate(sub,a,b)
elif o=="*": res=calculate(prod,a,b)
elif o=="/": res=calculate(div,a,b)
print(f"{a} {o} {b} = {res}")