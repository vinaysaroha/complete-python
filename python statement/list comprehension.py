# list comprehension is the unique way of quickly creating a list with python
# if you find yourself using a for loop along with .append() to create a list , List Comprehensions are good alternative

mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# below is list comprehension

mylist1 = [letter for letter in mystring]  # [element for element in list]
print(mylist1)

mylist1 = [x for x in range(0, 11) if x % 2 == 0]
print(mylist1)

result = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(result)

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)
