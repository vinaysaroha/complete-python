# tuples are very similar to list however they have one key defference - immutability
# once an element is inside a tuple it can not be reassigned
# tuple use parenthesis (1,2,3)
t = (1, 2, 3)
mylist = [1, 2, 3]
print(type(t))
print(type(mylist))
t = ('a', 4)
print(t[1])
t = ('a', 'a', 'a', 5, 7)
print(t.count('a'))
print(t.index('a'))
