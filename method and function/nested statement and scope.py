x = 25
def printer():
    x =50
    return x

print(printer())

# LEGB RULE
# L :Local -- Name assigned in any way within a function
# E: Enclosing function locals -- Name in the local scope of any and all enclosing functions, from inner to outer
# G: Global(Module)  -- Name assigned at the top level of a module file or declared global in a define within the file
# B: Built-in (Python) - Name preassigned in the built in the built in name module: open,range,SyntaxError

name = 'this is global string'
def greet():
    name = 'Sammy'
    def hello():
        print(f"hello {name}")
    hello()

greet()
