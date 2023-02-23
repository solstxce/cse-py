import re
lowc='[a-z]'
upc='[A-Z]'
s = input()
if re.search("[A-Za-z0-9]",s) == None:
    print(False)
else: print(True)
if re.search("[A-Za-z]",s) == None:
    print(False)
else: print(True)
if re.search("[0-9]",s) == None:
    print(False)
else: print(True)
if not re.search(lowc,s) == None:
    print(True)
else: print(False)
if not re.search(upc,s) == None:
    print(True)
else: print(False)