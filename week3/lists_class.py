#1
fruits=["apple","banana","cherry"]
print(fruits[2])
#2

print(f"Before: {fruits}")
fruits[0]="kiwi"
print(f"After: {fruits}")
#3
fruits.append("orange")
print(f"After: {fruits}")
#4
fruits.insert(1,"lemon")
print(f"After insert(): {fruits}")
#5
fruits.remove("banana")
print(f"After: {fruits}")
#6
print(f"Last element of the list: {fruits[-1]}")
7
print(f"{fruits[2:5]}")
#8
fruits=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(f"Length of the list: {len(fruits)}")
#9
fruits=["apple","banana","cherry","kiwi","melon","lemon"]
fruits=["apple","banana","cherry","orange","kiwi","melon","mango"]
#append
print(f"Before append(): {fruits}")
fruits.append("orange")
print(f"After append(): {fruits}")
#remove
print(f"Before remove(): {fruits}")
fruits.remove("melon")
print(f"After remove(): {fruits}")
#copy
fruits2=fruits.copy()
print(f"Original list: {fruits}")
print(f"Copied list: {fruits2}")
#count
print(f"The letter 'a' occured {fruits[0].count('a')} times in the word 'apple'")
#extend
print(f"Before extend(): {fruits}")
fruits.extend(fruits)
print(f"After extend(): {fruits}")
#insert
fruits=fruits2.copy()
print(f"Before insert(): {fruits}")
fruits.insert(1,"grapes")
print(f"After insert(): {fruits}")
#pop
print(f"Before pop(): {fruits}")
fruits.pop()
print(f"After pop(): {fruits}")
#index
print(f"Index of banana is {fruits.index('banana')}")
#sort
print(f"Sorted list: {fruits.sort()}")
#reverse
print(f"Reverse: {fruits.reverse()}")