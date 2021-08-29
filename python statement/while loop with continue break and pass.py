# While loops will continue to execute a block of code while some condition remains true.
"""
wile some_boolean_condition:
    do something
else:
    do something different
"""
x = 1
while x <= 10:
    print(f"I am good -----------> {x}")
    x += 1
else:
    print('x is greater than 10')

mylist=[1,2,3,4]
for number in mylist:
    if number == 3:
        continue
    print(number)

    if number == 2:
        pass # The pass statement is generally used as a placeholder i.e. when the user does not know what code to write.
    if number == 4:
       break


