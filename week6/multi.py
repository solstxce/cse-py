table=[]
n=4
lam=lambda n,i: table.append(f"{n} * {i} = {n*i}")
for i in range(1,11):
    lam(n,i)
for x in table:
    print(x)