from collections import Counter
def printallDuplicate(tu):
    c=Counter(tu)
    for key,value in c.items():
        print(key," Count:",value)
s=input()
printallDuplicate(s)


