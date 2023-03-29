vowels = 0
consonants = 0


def counter(string):
    global vowels
    global consonants
    for i in string.lower():
        if i in ["a", "e", "i", "o", "u"]:
            vowels += 1
        else:
            consonants += 1


string = input("Enter a string: ")
counter(string)
print("Vowels:", vowels)
print("Consonants", consonants)
