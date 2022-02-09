from random import randint
def makeEmail(name):
    fixedName = (name.replace(" ","")).lower()
    
    usedLetters = []
    email = ""
    
    for i in range(0,5):
        indexOfLetter = randint(0,(len(fixedName)-1))
        while (indexOfLetter in usedLetters):
            indexOfLetter = randint(0,(len(fixedName)-1))
            
        usedLetters.append(indexOfLetter)
        email += (fixedName[indexOfLetter])
        
    email += ("@calpoly.edu")
    return(email)
    
    
print(makeEmail(""))