def name(string):
    str_list=string.split(" ")
    str_list[0]=str_list[0].title()
    str_list[1]=str_list[1].title()
    string=" ".join(str_list)
    print(string)
namestr=input()
name(namestr)
