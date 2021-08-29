mylist = [1, 2, 3]
for num in range(0, 10, 2):
    print(num)

data = list(range(0, 11))
for num in data:
    print(num)

index_count = 0
for letter in 'abcde':
    print(f"{letter} ----------> {index_count}")
    index_count += 1

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

for letter in enumerate(word):
    print(letter)

for index, letter in enumerate(word):  # enumerate make tuple of every item with its index number
    print(index, '----------->', letter)

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c', 'd']

for item in zip(mylist1, mylist2):  # zip module pack the all iterable items in form of tuples
    print(item)

print(min(mylist1))
print(max(mylist1))

