def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)

num = 7
print("Factorial of",num,"is",fact(num))