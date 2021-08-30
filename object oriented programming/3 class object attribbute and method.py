################################## EXAMPLE 1 #############################################
class DogClass():
    species = 'Mammals'
    def __init__(self,breed,name,spot='No Spot'): #These are attribute other than self ,they not have () when they called
        self.breed = breed
        self.name = name
        self.spot = spot


    def force(self): # these are method (Operation/Action)
        print("Yes I am dog of Army")

    def local_dog(self,number): # no need to use self.number = number because it is provided by user after instance created under method
        print(f"I am local kutta and my number is {number}")
mydog = DogClass(breed='Lab',name='kalu')
print(mydog.species)
mydog.force()
mydog.local_dog(number=5)

##################################### EXAMPLE 2 #################################################

class Circle():
    # class object attribute
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    # METHODS
    def circumference(self):
        print(2*self.pi*self.radius)

    def area(self):
        print(self.pi*(self.radius**2))

my_result = Circle(radius=100)
my_result.area()
my_result.circumference()
print(my_result.radius)
print(my_result.pi)