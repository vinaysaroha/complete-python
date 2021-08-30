class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am Animal")

    def eat(self):
        print("I am eating")


my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()

print("########################################################")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):  # if you don't use this method than it will inherit method from Animal class you can check it by commenting this block
        print("I am a dog!!!")


mydog = Dog()
mydog.eat()
mydog.who_am_i()

print("##############################################################")


#################### Polymorphism Example ########################################
class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + "say woff!!!")


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + "say meow!!!")


niko = Dog('niko')
felix = Cat('felix')

niko.speak()
felix.speak()
print(
    "############################by polymorphism same task can be done by #####################################################################")
for pet in [niko, felix]:
    print(type(pet))
    pet.speak()


# or

def pet_speak(peter):
    peter.speak()


pet_speak(niko)
pet_speak(niko)
pet_speak(niko)
pet_speak(niko)
pet_speak(niko)
