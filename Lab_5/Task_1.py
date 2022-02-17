def chop(myList):
    if len(myList)>2:
        return [myList[0],myList[len(myList)-1]]
    else:
        return myList