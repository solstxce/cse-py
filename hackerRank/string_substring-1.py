def count_substring(string, sub_string):
    count=0
    i=0
    while i < len(string):
        if string[i]==sub_string[0]:
            if string[i:len(sub_string)+i]==sub_string:
                count+=1
        i+=1
    return count


string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)