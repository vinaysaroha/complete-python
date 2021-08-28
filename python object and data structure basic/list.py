# list are ordered sequence that can host varity of object they user [] bracket and commans to seperate objectss in
# the list list support indexing and slicing . List can be nested and also have a varity of useful method that can be
# called off of them
my_list = [1, 2, 4]
print(my_list)
my_list = ['string', 100, 10.2]
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[0:2])
second_list = ['one', 'two']
new_list = my_list + second_list
print(f'printing new list {new_list}')
new_list[0] = 0
print(f'modified list as list is mutable and it is order collection {new_list}')
new_list.append(6)
print(new_list)
new_list.pop()
print(new_list)
new_list.pop(0)
print(new_list)
new_list = ['a','g','z','r','q']
print(new_list)
new_list.sort() # sort method will work for same data type
print(new_list)
new_list.reverse()
print(new_list)

