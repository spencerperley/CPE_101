
class empl:
    employees = []
    

    def __init__(self, name, age):
        self.name = str(name)
        self.age = age 

        empl.employees.append(self)

    def __repr__(self):
        return str(self.name + " " + str(self.age))
    
    

    
def insertionSort(sortedList, func = lambda value : value):

    for i in range(1,len(sortedList)):
        key = func(sortedList[i])
        lock = sortedList[i]
        for j in range(0,i):
            comparator = func(sortedList[i-1-j])
            comparatorStore = sortedList[i-1-j]
            if key >= comparator:
                sortedList[i-j] = lock
                break
            else:
                sortedList[i-j] = comparatorStore
                if j == i-1 :
                    sortedList[0] = lock


empl("Michael", 45 )
empl("Jim",  35 )
empl("Pam", 30 )
empl("Dwight", 40 )
empl("Creed", 60)

insertionSort(empl.employees, func = lambda value : value.age)
print(empl.employees)

empl("Toby",45)

insertionSort(empl.employees, func = lambda value : value.age)
print(empl.employees)


def linearSearch(myList, key, func = lambda value : value):
    return [value for value in myList if func(value) == key][0]

print(linearSearch(empl.employees, 40 , func = lambda value : value.age))