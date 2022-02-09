def cumulative(myList):
    if myList:
        cumulativeList = [myList[0]]
        for i in range(1,len(myList)):
            cumulativeList.append(cumulativeList[i-1]+myList[i])
            
        return cumulativeList
    else:
        return []