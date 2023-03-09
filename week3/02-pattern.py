n=10
string="*"
i=1
for _ in range(1,10):
    if i<=5:
        for j in range(i):
            # if j==5:
            #     j=n-j-1
            print(string,end=" ")
        print()
    else:
        for j in range(n-i):
            # if j==5:
            #     j=n-j-1
            print(string,end=" ")
        print()
    i+=1
            
