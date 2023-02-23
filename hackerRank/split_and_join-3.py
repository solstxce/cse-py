def split_and_join(string):
    string=string.split(" ")
    string="-".join(string)
    return string
string=input()
res=split_and_join(string)
print(res)