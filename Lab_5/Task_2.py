def calcAvererage(myList):
    sum = 0
    for value in myList:
        sum += value
    
    return (sum/len(myList))