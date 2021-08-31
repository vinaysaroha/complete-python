# Decorator allow you to "decorate" a function
# Imagine you created a function

def simple_function():
    # do Simple stuff
    return "something"

# You now have two option
# add that extra code (functionality) to your old function.
# create a brand new function that contains the old code and then add new code to that


def func1():
    print("1")

func1()

def hello():
    print("Hello")

hello()

new_hello = hello
print("#######################################")
del hello
new_hello()







def hello(name='vinay'):
    print(f"hello {name}")

    def new_hello():
        print("this is new hello function")
    new_hello()

    def welcome():
        print("Welcome")
    welcome()

hello()



print("####################################################################################")

def Hello():
    return  'Hi Jose!'

def Other(som_def_func):
    print('other code run here')
    print(som_def_func())
Other(Hello)


###################################Decorator#################################################
print("#######################################################################################")
def new_decorator(orignal_function):
    def wrap_function():
        print("some extra code before orignal function")
        orignal_function()
        print('some extra code after orignal function')
    return wrap_function

def function_needs_decorator():
    print("I want to be decorator")

print(new_decorator(function_needs_decorator))
dec_fun = new_decorator(function_needs_decorator)

@new_decorator
def function_needs_decorator():
    print("I want to be decorator")

function_needs_decorator()



