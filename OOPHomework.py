# Importing cmath due to bug in math not letting me use .sqrt
from math import sqrt

# Creating class to create custom methods for distance and slope
class Line():
    
    def __init__(self,coordinate1,coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2
        
    # Creating distance method and how it should behave
    def distance(self):
        
        # Rewrote math formula in steps when I noticed it wasn't displaying correct result based on course example
        stepOne = (coordinate1[0] - coordinate2[0])
        
        stepTwo = (coordinate1[1] - coordinate2[1])
        
        stepThree = ((stepOne) ** 2) + ((stepTwo) ** 2)
        
        stepFour = sqrt(stepThree)
        
        print(stepFour)
        
        # Math formula to figure out what the distance is
       # print(sqrt((coordinate1[0] - coordinate2[0]) ** 2 + (coordinate1[1] - coordinate2[1] ** 2)))
        
       
    # Math formula for slopes 
    def slope(self):
        
        # Having same problems as above with distance 
        print((coordinate2[1] - coordinate1[1]) / (coordinate2[0] - coordinate1[0]))
        

# Variable assignment 
coordinate1 = (3,2)
coordinate2 = (8,10)

# Assigning class to test variable 
test = Line(coordinate1,coordinate2)

# Printing results
print(test.distance(), test.slope())