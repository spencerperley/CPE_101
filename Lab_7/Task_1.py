class Shape:
    def __init__(self,name,dim):
        self.name = name
        self.dim = dim

class Dimension:
    def __int__(self,a,b):
        self.a = a
        self.b = b

Geometric_Shapes = [         
Shape('rectangle', [Dimension(5,6), Dimension(14,7), Dimension(5,2)]), 
 
Shape('square', [ Dimension(5,5), Dimension(4.2,4.2)]), 
 
Shape('ellipse', [Dimension(5,6), Dimension(7,7)]), 
]       
 
 
 
