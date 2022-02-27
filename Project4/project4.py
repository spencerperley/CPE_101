import sys, os, re

# I used this .ppm viewer https://marketplace.visualstudio.com/items?itemName=martingrzzler.simple-ppm-viewer
# it is the not the one that is specified in the lab however it is a lot easier to use as it just works in tandem with the text editor I am using.

#*** My note to the grader: *** Im not sure if this is a windows specific path settup but it works on my computer so hopefully it should work. 
# I took the directory thing from stack overflow and cited it as best I could as there were no directions on citing open source code in the syllabus that I could find.

#*** Second note *** So I was having issues with opening files in this project and the past project so i did some fixing by including the full path 
# in the open() string. now I was doing that because I have my whole CPE_101 folder open which has sub folders and that meant the files I was trying to access weren't exposed to the path that the interpreter was looking in 
# now I realize this now after writing the code but I learned a good deal about how the windows file system, terminal and python terminal work.
# so I know a lot of the stuff in here is now kind fluff that I did to get around that but it also has some nice features like screening the curret directory to make sure the correct file is there.
# I just wanted to leave this note here to explain why it is more complicated and dirty than it should be. 


directoryPath = os.path.dirname(os.path.abspath(sys.argv[0])) # I got this from this https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-the-currently-running-scrip


def takeValue(message,acceptableInputs = [], errorText = "error: input incorrect, try again", fileName = False):
    """This function screens inputs until a suitable input is found"""
    while True:
        inputValue = input(message)
        if fileName:
            inputValue.replace(" ","_")
        if re.fullmatch("[a-zA-Z0-9_ .]+",inputValue): # simple regular expression to weed out anything that is not an approved character
            if not(acceptableInputs): # if the acceptabel imputs list is empty then any input is accepted 
                return(inputValue)
            elif inputValue in acceptableInputs:
                return(inputValue)
            else:
                print(errorText)
        else:
            print("Inputs must only contain letters, numbers, black space, periods, or underscores")
        
"""takes the input from the user and checks it against the current directory to see if there is an aceptabel file"""
inputFileName = directoryPath + "\\" + (takeValue("Enter the name of the file you wish to be altered: ", [value.replace(".ppm", "") for value in os.listdir(
    directoryPath) if ".ppm" in value], errorText="Input Incorrect, make sure the file you want is in the same directory as this script and that it is a .ppm file. \nFile name should not in include the .ppm when entered.\nfor example the file at c:\\Project4\\myImage.ppm should be entered as: myImage", fileName=True) + ".ppm")

"""takes the input from the user to get the name of their desired output file"""
outFileName = directoryPath + "\\" + \
    (takeValue("Enter the name of the file you wish output the data to: ", fileName=True) + ".ppm")

"""takes the input from the user and checks it against the acceptabel requests."""
operation = takeValue("Which of the following commands do you wish to use to alter your image:\n'negate'\n'high contrast'\n'gray scale'\n'remove <color>' where <color> is 'red' 'green' or 'blue' \n: ", [
                      'negate', 'high contrast', 'gray scale']+[('remove ' + value) for value in ["red", "green", "red"]])


inputFile = open((inputFileName), "r")
outFile = open((outFileName), "w")


def ppmToArray(inputFile):
    """converts the .ppm file to a specially formated array for ease of use returns in the form [[width,hight],[redValue,greenValue,blueValue,....]"""
    rows = [value[0:len(value)-1] for value in inputFile.readlines()]
    size = (rows[1].split(" "))
    data = (size,[value.split(" ") for value in rows[3::]])
    
    return(data)

    
def arrayToPPM(myList, sizeKey, outFile = outFile, encodingSpecKey = "P3", rangeKey = 255):
    """This function takes a file name and the desired list and writes the data to a file in the correct .ppm format"""
    outFile.seek(0,0)
    outFile.write("\n".join([encodingSpecKey, " ".join([str(sizeKey[0]),str(sizeKey[1])]), str(rangeKey)] + [" ".join([str(subValue) for subValue in value]) for value in myList])) #list copression is dirty because each value has to be a string
    outFile.close()
    
    


def negate_image(inputFile = inputFile, outFile = outFile):
    """This takes the input and output files and then negates each color value and then writes that to the output file"""
    data = ppmToArray(inputFile)
    image = data[1]
    for i in range(0,int(data[0][1])):
        for j in range(0,int(data[0][0])*3):
            image[i][j] = abs(int(image[i][j])-255)
    arrayToPPM(image, data[0], outFile = outFile )
        


def greyScale(inputFile = inputFile, outFile = outFile):
    """This takes the input and output file and sets every triplet to the average of the triplet"""
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
    """This takes the input and output files and for every value if it is above 127 it sets it to zero if it is above it sets it to 255"""
    data = ppmToArray(inputFile)
    image = data[1]
    for i in range(0,int(data[0][1])):
        for j in range(0,int(data[0][0])*3):
            image[i][j] = 255 if int(image[i][j]) > 127 else 0
            
    arrayToPPM(image, data[0], outFile = outFile )
    
def removeOne(pos, inputFile = inputFile, outFile = outFile):
    """This function is what is called for each of the remove <color> functions and it takes the input file the output file and the position in the color triplet that should be set to zero and changes that to zero in the output file"""
    data = ppmToArray(inputFile)
    image = data[1]
    for i in range(0,int(data[0][1])):
        for j in range(0,int(data[0][0])):
            image[i][(j*3)+pos] = 0
    arrayToPPM(image, data[0], outFile = outFile)
    
def removeRed(inputFile = inputFile, outFile = outFile):
    """This function calls the remove one function with the position zero in order to remove red from the file"""
    removeOne(0, inputFile = inputFile, outFile = outFile)
    
#removeRed(inputFile = inputFile, outFile = outFile)

def removeGreen(inputFile = inputFile, outFile = outFile):
    """This function calls the remove one function with the position one in order to remove green from the file"""
    removeOne(1, inputFile = inputFile, outFile = outFile)
    
#removeGreen(inputFile = inputFile, outFile = outFile)
    
def removeBlue(inputFile = inputFile, outFile = outFile):
    """This function calls the remove one function with the position two in order to remove blue from the file"""
    removeOne(2, inputFile = inputFile, outFile = outFile)

#removeBlue(inputFile = inputFile, outFile = outFile)

"""This set of conditionals calls the corresponding function based off of the operation that was requested by the user and then prints a message as well as the path to the file"""

if operation == 'negate':
    negate_image(inputFile = inputFile, outFile = outFile)
    print(f"Your file has been negated and has been saved at this location: {outFileName}")
    
elif operation == 'high contrast':
    highContrastImage(inputFile = inputFile, outFile = outFile)
    print(f"Your file has been converted to hight contrast and has been saved at this location: {outFileName}")
    
elif operation == 'gray scale':
    greyScale(inputFile = inputFile, outFile = outFile)
    print(f"Your file has been converted to grey scale and has been saved at this location: {outFileName}")
    
elif operation == "remove red":
    removeRed(inputFile = inputFile, outFile = outFile)
    print(f"Your file has had the red removed and has been saved at this location: {outFileName}")
    
elif operation == "remove green":
    removeGreen(inputFile = inputFile, outFile = outFile)
    print(f"Your file has had the green removed and has been saved at this location: {outFileName}")
    
elif operation == "remove blue":
    removeBlue(inputFile = inputFile, outFile = outFile)
    print(f"Your file has had the blue removed and has been saved at this location: {outFileName}")


inputFile.close()