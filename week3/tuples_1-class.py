fruits=("apple","banana","cherry","orange","kiwi","melon","mango")
#1
print("First element is:",fruits[0])
#2
print("No.of items in tuple:",len(fruits))
#3
print(f"The last element: {fruits[-1]}")
#4
print(f"Elements from start to kiwi: {fruits[:4]}")
#5
print(f"Elements from cherry to end: {fruits[2:]}")
#6
print(f"Elements from -4 to -1: {fruits[-4:-1]}")
#7
if "apple" in fruits:
    print("Yes, 'apple' is in the tuple.")
else:
    print("No, 'apple' is not in the tuple.")
#8
fruits=list(fruits)
fruits.append("orange")
fruits=tuple(fruits)
print("Changed tuple:",fruits)
#9
fruits2=("lemon",)
fruits+=fruits2
print("Tuple addition:",fruits)
#10
fruits=list(fruits)
fruits.remove("apple")
fruits=tuple(fruits)
print("Changed tuple:",fruits)