from cmath import sqrt

class Line():
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    
    def distance(self):
        stepOne = (coordinate1[0] - coordinate2[0])
        
        stepTwo = (coordinate1[1] - coordinate2[1])
        
        stepThree = ((stepOne) * 2) + ((stepTwo) * 2)
        
        stepFour = sqrt(stepThree)
        
        print(sqrt((coordinate1[0] - coordinate2[0]) * 2 + (coordinate1[1] - coordinate2[1] * 2)))
        print(stepFour)
       

    def slope(self):
        
        print((coordinate2[1] - coordinate2[0]) / (coordinate1[1] - coordinate1[0]))

coordinate1 = (2,4)
coordinate2 = (1,7)
test = Line(coordinate1,coordinate2)
print(test.distance(), test.slope())