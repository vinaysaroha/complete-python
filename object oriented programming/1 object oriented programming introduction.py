# object oriented programming allow programmers to create their own objects that have method and attributes .
# Recall that after defining a string ,list, dictionary, or other objects you were able to call methods off them with the .method_name() syntax

# These method act as function that use information about the objects as well as the objects as well as the object itself to return results or change the current object

class NameOfClass():
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param1)
