def func():
    print("func in one.y")

print("Top level in one.py")

if __name__ == '__main__':  # if someone execute one.py directly then it will run if condition . if some one import one.py file then it will run else condition .
    print('one.py is run directly')
else:
    print('one.py has been imported')
