import re
s = input()
print("Is alpha numeric: ",end="")
if re.search("[A-Za-z0-9]",s) == None:
    print(False)
else: print(True)
print("Contains alphabets: ",end="")
if re.search("[A-Za-z]",s) == None:
    print(False)
else: print(True)
print("Contains numbers: ",end="")
if re.search("[0-9]",s) == None:
    print(False)
else: print(True)
print("Contains Lower Case: ",end="")
if not re.search("[a-z]",s) == None:
    print(True)
else: print(False)
print("Contains Upper Case: ",end="")
if not re.search("[A-Z]",s) == None:
    print(True)
else: print(False)
