# dictionaries are un-order mapping for storing objects .
# the key value pair allow users to quickly grab objects without needing to know an index location
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(my_dict)
print(my_dict['key1'])
print(my_dict.values())
my_dict = {'list1': [[100, 5, 6, 7], 2, 3], 'list2': [0, 1, 2]}
print(my_dict['list1'][0])
my_dict['list1'][0].sort()
print(my_dict['list1'][0])
my_dict['list3'] = [6, 3, 5, 8]
print(my_dict)


