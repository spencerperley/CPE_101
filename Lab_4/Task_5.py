
def findSubstring(sub, myStr):
    pIndex = -1
    tempString = myStr
    for letter in sub:
        index = tempString.find(letter)

        if index <= pIndex:
            return False
        else:
            tempString = tempString[(index+1):]
            
    return True



