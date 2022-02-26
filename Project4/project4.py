import sys, os, re

from numpy import average

# I used this .ppm viewer https://marketplace.visualstudio.com/items?itemName=martingrzzler.simple-ppm-viewer


#*** My note to the grader: *** Im not sure if this is a windows specific path settup but it works on my computer so hopefully it should work. 
# I took the directory thing from stack overflow and cited it as best I could as there were no directions on citing open source code in the syllabus that I could find.

directoryPath = os.path.dirname(os.path.abspath(sys.argv[0])) # I got this from this https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-the-currently-running-scrip


inputFileName = directoryPath + "\\" + "ny.ppm"
outFileName = directoryPath + "\\" + "red.ppm"
#outFileName = directoryPath + "\\" + "green.ppm"
#outFileName = directoryPath + "\\" + "blue.ppm"



def takeValue(message,acceptableInputs = [], errorText = "error: input incorrect, try again", fileName = False):
    """This function screens inputs until a suitable input is found"""
    while True:
        inputValue = input(message)
        if fileName:
            inputValue.replace(" ","_")
        if re.fullmatch("[a-zA-Z0-9_ ]+",inputValue): # simple regular expression to weed out anything that is not an approved character
            if not(acceptableInputs): # if the acceptabel imputs list is empty then any input is accepted 
                return(inputValue)
            elif inputValue in acceptableInputs:
                return(inputValue)
            else:
                print(errorText)
        else:
            print("Inputs must only contain letters, numbers, black space, or underscores")
        
inputFileName = directoryPath + "\\" + (takeValue("Enter the name of the file you wish to be altered",[value.replace(".ppm","") for value in os.listdir(directoryPath) if ".ppm" in value],errorText="Input Incorrect, make sure the file you want is in the same directory as this script",fileName=True)+ ".ppm")
outFileName = directoryPath + "\\" + (takeValue("Enter the name of the file you wish output the data to",fileName=True) + ".ppm")
operation = takeValue("Which of the following commands do you wish to use to alter your image:\n'negate'\n'high contrast'\n'gray scale'\n'remove <color>' where <color> is 'red' 'green' or 'blue'",['negate','high contrast','gray scale']+[('remove ' + value) for value in ["red","green","red"]])




inputFile = open((inputFileName), "r")
outFile = open((outFileName), "w")


def ppmToArray(inputFile):
    """converts the .ppm file to a specially formated array for ease of use"""
    rows = [value[0:len(value)-1] for value in inputFile.readlines()]
    size = (rows[1].split(" "))
    image = (size,[value.split(" ") for value in rows[3::]])
    
    return(image)

    
def arrayToPPM(myList, sizeKey, outFile = outFile, encodingSpecKey = "P3", rangeKey = 255):
    """This function takes a file name and the desired list and writes the data to a file in the correct .ppm format"""
    outFile.seek(0)
    outFile.write("\n".join([encodingSpecKey, " ".join([str(sizeKey[0]),str(sizeKey[1])]), str(rangeKey)] + [" ".join([str(subValue) for subValue in value]) for value in myList])) #list copression is dirty because each value has to be a string
    outFile.close()
    
    


def negate_image(inputFile = inputFile, outFile = outFile):
    data = ppmToArray(inputFile)
    image = data[1]
    for i in range(0,int(data[0][1])):
        for j in range(0,int(data[0][0])*3):
            image[i][j] = abs(int(image[i][j])-255)
    arrayToPPM(image, data[0], outFile = outFile )
        


def greyScale(inputFile = inputFile, outFile = outFile):
    data = ppmToArray(inputFile)
    image = data[1]
    for i in range(0,int(data[0][1])):
        for j in range(0,int(data[0][0])):
            sum = 0
            for k in range(0,3):
                sum += int(image[i][(j*3)+k])
            for k in range(0,3):
                image[i][(j*3)+k] = sum//3
                
    arrayToPPM(image, data[0], outFile = outFile)



def highContrastImage(inputFile = inputFile, outFile = outFile):
    data = ppmToArray(inputFile)
    image = data[1]
    for i in range(0,int(data[0][1])):
        for j in range(0,int(data[0][0])*3):
            image[i][j] = 255 if int(image[i][j]) > 127 else 0
            
    arrayToPPM(image, data[0], outFile = outFile )
    
def removeOne(pos, inputFile = inputFile, outFile = outFile):
    data = ppmToArray(inputFile)
    image = data[1]
    for i in range(0,int(data[0][1])):
        for j in range(0,int(data[0][0])):
            image[i][(j*3)+pos] = 0
    arrayToPPM(image, data[0], outFile = outFile)
    
def removeRed(inputFile = inputFile, outFile = outFile):
    removeOne(0, inputFile = inputFile, outFile = outFile)
    
#removeRed(inputFile = inputFile, outFile = outFile)

def removeGreen(inputFile = inputFile, outFile = outFile):
    removeOne(1, inputFile = inputFile, outFile = outFile)
    
#removeGreen(inputFile = inputFile, outFile = outFile)
    
def removeBlue(inputFile = inputFile, outFile = outFile):
    removeOne(2, inputFile = inputFile, outFile = outFile)

#removeBlue(inputFile = inputFile, outFile = outFile)

if operation == 'negate':
    negate_image(inputFile = inputFile, outFile = outFile)
elif operation == 'high contrast':
    highContrastImage(inputFile = inputFile, outFile = outFile)
elif operation == 'gray scale':
    greyScale(inputFile = inputFile, outFile = outFile)
elif operation == "remove red":
    removeRed(inputFile = inputFile, outFile = outFile)
elif operation == "remove green":
    removeGreen(inputFile = inputFile, outFile = outFile)
elif operation == "remove blue":
    removeBlue(inputFile = inputFile, outFile = outFile)



inputFile.close()