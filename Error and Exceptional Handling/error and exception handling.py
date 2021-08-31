# We use three keywords for this:
# try: this is the block of code to be attempted(may lead to an error)
# except: Block of code will execute in case there is an error in try block
# finally: A final block of code to be executed , regardless of an error
try:
    def adding_numbers(num1,num2):
        print(num1+num2)

    adding_numbers(10,'20')
    print("under try")
except Exception as ex:
    print(ex)

finally:
    print("this is finally block")