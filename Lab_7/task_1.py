from cmath import pi


class Shape:
    
    def __init__(self,name,dim):
        
        self.name = name
        self.dim = dim

        
class Dimension:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __repr__(self):
        return str(str(self.a) + str(self.b))
        

Geometric_Shapes = [         
Shape('rectangle', [Dimension(5,6), Dimension(14,7), Dimension(5,2)]), 
 
Shape('square', [ Dimension(5,5), Dimension(4.2,4.2)]), 
 
Shape('ellipse', [Dimension(5,6), Dimension(7,7)]), 
]

# print([dim for shape in Geometric_Shapes for dim in shape.dim if (shape.name == 'square' or shape.name == 'rectangle')])

def calArea(name, li = Geometric_Shapes):
    
    if name == "rectangle":
     
        return f"{max([dim.a*dim.b for shape in li for dim in shape.dim if shape.name == name])} is the max area amongst all shapes of type: {name}"
    if name == "square":
        
        return f"{max([dim.a*dim.b for shape in li for dim in shape.dim if shape.name == name])} is the max area amongst all shapes of type: {name}"
    if name == "ellipse":
        
        return f"{max([dim.a*dim.b*pi for shape in li for dim in shape.dim if shape.name == name])} is the max area amongst all shapes of type: {name}"
    
print(calArea("rectangle", li = Geometric_Shapes))