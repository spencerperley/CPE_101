from random import randint

names = ["ada lovelace" , "grace hopper" , "barbara liskov"] 
fixedNames = []
for name in names:
    fixedName = name.replace(" ","")
    fixedNames.append(fixedName)

for name in fixedNames:
    usedLetters = []
    email = ""
    
    for i in range(0,5):
        indexOfLetter = randint(0,(len(name)-1))
        while (indexOfLetter in usedLetters):
            indexOfLetter = randint(0,(len(name)-1))
            
        usedLetters.append(indexOfLetter)
        email += (name[indexOfLetter])
        
    email += ("@calpoly.edu")
    print(email)