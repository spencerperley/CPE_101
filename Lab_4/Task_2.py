def cumulative(myList):
    if myList:
        cumList = [myList[0]]
        for i in range(1,len(myList)):
            cumList.append(cumList[i-1]+myList[i])
            
        return cumList
    else:
        return []