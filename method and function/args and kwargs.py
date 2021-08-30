def function1(*args):  # args kitne bhi item le sakta hai but sare item , ke sath hone chaheye
    print(sum(args))


function1(1, 2, 3, 4)


def function2(**kwargs):  # keyword arguments
    if 'fruit' in kwargs:
        print(kwargs['fruit'])


function2(fruit='apple')


def function3(*args, **kwargs):
    print(f"Your first item is {args[0]},{kwargs['food']}")


function3(1, 2, 3, food='pratha')

