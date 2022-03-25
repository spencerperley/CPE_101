def remove(myList):
    return [a for a in myList if a > 0]

b = [1,3,5,-3,43,-7]

print(remove(b))