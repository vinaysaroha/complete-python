from collections import Counter
mylist = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3]
# count unique item from the list

print(Counter(mylist))



letter = 'aaaaabbbbbbbbccccccccccccc'
print(Counter(letter).most_common()) # to get output in form of list of tuple

print(list(Counter(letter)))

