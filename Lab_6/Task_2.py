class MyUberCar:
    def __init__(self,model,color,maxVelocity,destination,year):
        self.model = model
        self.color = color
        self.maxVelocity = maxVelocity
        self.destination = destination
        self.year = year
        
myCar = MyUberCar(input("Enter car model:"),input("Enter car color:"),int(input("Enter speed limit or velocity:")),input("Enter destination:"),int(input("Enter car manufacturing year:")))