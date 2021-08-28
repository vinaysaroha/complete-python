file = open('sample_file.txt', 'w')
file.write('hello every this is sample file to check input and output with basic file in python')
file.close()
print(file.closed)

file = open('sample_file.txt', 'r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

new_file = open('sample_file.txt', 'w')
new_file.writelines('''
hello every one 
how are you all
thanks for using i/o in python
''')
new_file.close()
print(new_file.closed)

new_file = open('sample_file.txt', 'r')
print(new_file.readlines())
new_file.close()


with open('sample_file.txt','r') as file:
    print(file.readlines())


with open('sample_file.txt',mode='a') as file:
    file.write('''
this is appended lines
so be calm''')

with open('image.jpg',mode='rb') as image:
    image.read()
