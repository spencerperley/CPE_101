def insertionSort(myList):
    for i in range(1,len(myList)):
        key=myList[i]
        for j in range(0,i):
            comparator = myList[i-1-j]
            if key >= comparator:
                myList[i-j] = key
                break
            else:
                myList[i-j] = comparator
                if j == i-1 :
                    myList[0] = key

from random import randint

myList = []
for i in range(0,1000):
    myList.append(randint(1,1000))
print (myList)
testerList = sorted(myList)

insertionSort(myList)

if testerList == myList:
    print("Pass")
    print(myList)
