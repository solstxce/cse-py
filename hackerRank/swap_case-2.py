def swap_case(string):
    string=[letter for letter in string]
    for i in range(0,len(string)):
        if string[i].isalpha():
            if string[i].isupper():
                string[i]=string[i].lower()
            else:
                string[i]=string[i].capitalize()
    string="".join(string)
    return string
string=input()
res=swap_case(string)
print(res)