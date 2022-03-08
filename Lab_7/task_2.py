class empl:
    employees = []
    emplSorted = []

    def __init__(self, name, age):
        self.name = name
        self.age = age 

        empl.employees.append(self)

    def __repr__(self):
        return str(self.name + " " + str(self.age))

    
def insertionSort(myList, Key = None):

    if Key:
        keyDict = {}
        sortedList = insertionSort(keyList)
    else:
        sortedList = myList.copy()
        for i in range(1,len(sortedList)):
            key=sortedList[i]
            for j in range(0,i):
                comparator = sortedList[i-1-j]
                if key >= comparator:
                    sortedList[i-j] = key
                    break
                else:
                    sortedList[i-j] = comparator
                    if j == i-1 :
                        sortedList[0] = key
    return sortedList

a= empl("a",1)
b= empl("b",5)
c= empl("c",3)


print(insertionSort(empl.employees, Key = lambda e : e.age))