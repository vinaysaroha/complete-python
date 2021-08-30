def function1(num):
    return num ** 2


my_list = [1, 2, 3, 4, 5]

print(list(map(function1, my_list)))


def check_even_number(num):
    return num % 2 == 0


print(list(filter(check_even_number, my_list)))


###############################################################################
########################LAMDA FUNCTION###########################################

def square(num):
    result = num ** 2
    return result


# this above function can also be written
def square(num):
    return num ** 2


#       or

# in lamda function def keyword and name(square) are replaced by lamda keyword and their is no return keyword requred because in lamda function after : what ever be is it will return it

squared = lambda num: num ** 2
print(squared(5))

print(list(map(lambda num: num ** 2, my_list)))
