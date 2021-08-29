# control flow syntax make use of colons and indentation(white space).
# if some_condition:
#   execute some code
# else:
#   do something else
if True:
    print("it's True")

hungry = True
if hungry:
    print("Feed me!")

hungry = False
if hungry:  # (if hungry == True) == (if hungry)
    print("Please Feed Me!")
else:
    print("I am not hungry")

loc = 'Bank'
if loc == 'Auto Shop':
    print("car is cool")
elif loc == 'Bank':
    print("Money is cool")
else:
    print("I don't know Much")
