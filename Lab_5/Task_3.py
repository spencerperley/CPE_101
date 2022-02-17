def filter_pallendromes(myList):
    return [value for value in myList if (value[0]+value[1])==(value[4]+value[3])]
