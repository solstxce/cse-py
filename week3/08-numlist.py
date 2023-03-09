n=int(input("Enter a number: "))
for i in range(1,n+1):
    isPrime=True
    for x in range(2,int(i/2)+1):
        if i%x==0:
            isPrime=False
            break
    if not isPrime:
        print(i)