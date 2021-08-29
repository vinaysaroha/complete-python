# the term iterable means you can "iterate" over the object. for example you can iterate over every character in a
# string, iterate over every item in a list , iterate over every key in a dictionary
"""
syntax of a for loop :
my_iterable=[1,2,3]
for item_name in my iterable:
    print(item_name)
"""
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    print(num)

for item in mylist:
    print("hello")

for item in mylist:
    if item % 2 == 0:
        print(f"{item} is even number")
    else:
        print(f"{item} is odd number")

list_sum = 0

for num in mylist:
    list_sum += num
print(f"{list_sum} is the total of you list")

mystring = "Hello World"
for letter in mystring:
    print(f"{mystring.index(letter)}  -------> {letter}")

mylist = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
for (a, b) in mylist:  # this is called tuple unpacking in for loop
    print(a)
    print(b)

mydict = {'key1': 4, 'key2': 3, 'key3': 2, 'key4': 9}
for item in mydict.items():
    print(item)

for key, value in mydict.items():
    print(value,'\n')

for item in mydict.values():
    print(item)


