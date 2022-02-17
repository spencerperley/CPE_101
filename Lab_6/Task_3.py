class womenScientists:
    allWomenSci = []

    def __init__(self, name, city, contry, birthYear):
        self.name = name
        self.city = city
        self.contry = contry
        self.birthYear = birthYear
        self.achievements = []

        womenScientists.allWomenSci.append(self)

    def birthPlace(self):
        print(self.city + " " + self.contry + " " + self.birthYear)
        
    def addAchievement(self,achievement):
        self.achievements.append(achievement)
        
    def makeGreat():
        for scientist in womenScientists.allWomenSci:
            scientist.name = "The Great" + \
                " " + scientist.name[0] + scientist.name[scientist.name.find(" "):len(scientist.name)]
            
        
    def showWomenScientists(test = False):
        if not(test):
            for scientist in womenScientists.allWomenSci:
                print(scientist.name + " " + scientist.achievements[0])  
        else:
            testReturnList = []
            for scientist in womenScientists.allWomenSci:
                testReturnList.append(str(scientist.name + " " + scientist.achievements[0])) 
            return testReturnList 
                




