def print_full_name(f_name,l_name):
    full=f_name+" "+l_name
    string=f"Hello {full}! You just delved into python."
    return string
f_name=input("Enter first name: ")
l_name=input("Enter last name: ")
res=print_full_name(f_name, l_name)
print(res)
