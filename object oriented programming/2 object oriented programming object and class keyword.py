class Sample():
    pass


first_instance = Sample()
print(type(first_instance))

class Dog():
    def __init__(self,breed):
        self.breed = breed
        print(id(self))
        print(id(self.breed))

dog = Dog('Lab')
print(dog.breed)
print(id(dog))
print(id(dog.breed))

print("#################################################################")
class MyClass():
    def __init__(self,mymethod1):
        self.method1=mymethod1  # method jo user ko show hoga wo method1 hoga
                                # mymethod1 to programer ne apne sahuliat ke liye likha hai sath he sath he instance bnate time jab constructer ko call karega () tab uske under show hoga ke usko value kya chahey

first_class = MyClass('data1')
print(first_class.method1)


first_class = MyClass('data')
print(first_class.method1)


class MyDog():
    def __init__(self,breed,name,spot='No spots'):
        self.breed = breed
        self.name = name
        self.spot = spot



first_dog = MyDog(breed='Lab',name='Kalu',spot='Yes')
print(first_dog.breed)
print(first_dog.name)
print(first_dog.spot)