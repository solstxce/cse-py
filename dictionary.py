#1
s={i:i*i for i in range(1,16)}
print(s)
#2
# Write a Python program to iterate over dictionaries using for loops.
d={"a":1,"b":2,"c":3}
print("Items in dictionary:")
for i in d:
    print(i,d[i])
#3
d= {0: 10, 1: 20}
s=input("Enter key to add: ").strip()
v=input("Enter value: ").strip()
d[s]=v
print(d)
#4
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
#5
d={"a":1,"b":2,"c":3}
k=input("Enter key to check: ")
if k in d.keys():
    print("Is present")
else:
    print("Is not present")
#8
#  Write a Python program to remove a key from a dictionary.
d={"a":1,"b":2,"c":3}
k=input("Enter key to remove: ").strip()
d.pop(k)
print(f"Updated dict: {d}")
