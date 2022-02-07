def middle(myList):
    if len(myList) > 2:
        newList = myList.copy()
        newList.pop(0)
        newList.pop(len(myList)-2)
        
        return newList
    else:
        return myList.copy()