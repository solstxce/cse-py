import re
string=input()
string=re.split(r"[.,]", string)
for i in string:
    print(i)