l = ["a", "b", "c", "d"]
n = "e"


def search(x):
    global n
    if x == n:
        return True
    else:
        return False


present = list(filter(search, l))
if present == "[]":
    print(f"{n} not in the given list.")
else:
    print(f"{n} is in given list.")
