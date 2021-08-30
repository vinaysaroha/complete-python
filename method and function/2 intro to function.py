# creating clean repeatable code is a key part of becoming an effective programmer.
# Function allow ys to create block of code that can be easily executed many times , without needing to contantly rewrite the entire block of code
# creating a function require a very specific syntax including the def keyword correct indentation and proper structure.
# syntax : def name_of_function(name):  ----> always use snake casing
#             """
#                   Doc string explain function
#             """
#               print(f"hello {name}")  -----> it will just print the output
#               return f"hello {name}"  -----> always return the output and you can save the result to some other variable
###############################################################################
def say_hello():
    print("Hello")
    print("Hi, How are you ")


say_hello()  # ---> to execute the function you should use ()
print(
    say_hello)  # if you not use () then it will tell that say hello function is a function and its value its value store in ram at 0xxxxx location


#######################################################################################

def say_hello(name='Default'):  # if in case name is not provided than it will take Default value
    print(f"hello {name}")


say_hello()
say_hello('vinay')


######################################################################################
def function1(name):
    return f"Hello {name}"


data1 = function1('vinit')
print(data1)

#####################################################################################
data1 = say_hello('rahul')
print(data1)
print(type(data1))


######################################################################################
def check_even_num(provide_list):
    """
    this will print even number from the list
    :param provide_list:
    :return: list of even number
    """
    even_list = []
    for num in provide_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            pass
    print(even_list)


check_even_num([1, 2, 3, 4, 5])
#######################################################################################

stock_price = [('Gold', 50000), ('Silver', 32000), ('Platinum', 40000)]


def stock(item_list):
    """
    checking the price of all item in stock market
    :param item_list is to be passed
    :return: (item,price)
    """
    while True:
        data1 = ''
        metal = input("Enter the item name of which you want to know the detail: ")
        for item, price in item_list:
            if metal == item:
                print(f"{item} price is {price}")
                data1 = 'False'
                break
        if data1 == 'False':
            break


stock(stock_price)
