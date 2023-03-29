roll = [1, 3, 4, 7, 8, 11, 12, 13, 16, 18, 19, 24, 25]
def isPresent(n):
    if n in roll:
        return True
    else: return False
n=int(input("Roll No: "))
if isPresent(n):
    print("The student is present.")
else:
    print("The student is not present.")