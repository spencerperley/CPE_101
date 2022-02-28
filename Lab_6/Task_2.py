class MyUberCar:
    def __init__(self,model,color,maxVelocity,destination,year):
        self.model = model
        self.color = color
        self.maxVelocity = maxVelocity
        self.destination = destination
        self.year = year
    def timeToDestinatino(self):
        if self.destination == "Pismo":
            return "25 minutes"
        elif self.destination == "Airport":
            return "10 minutes"
        elif self.destination == "Hospital":
            return "12 minutes"
myCar = MyUberCar(input("Enter car model:"),input("Enter car color:"),int(input("Enter speed limit or velocity:")),input("Enter destination:"),int(input("Enter car manufacturing year:")))