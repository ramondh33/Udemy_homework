class Dog():
    
    #class object attribute same for any instance of a class
    
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
        
    # Operations/Actions ---> Methods
    def bark(self):
        print("WOOF! My name is {}".format(self.name))

myDog = Dog('Lab',"Tyson")

print(myDog.breed, myDog.name, myDog.species)
print(myDog.bark())
