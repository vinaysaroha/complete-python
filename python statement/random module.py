from random import shuffle, randint

list1 = [1, 2, 3]
while True:
    game_input = int(input("Enter number between 1 to 3: "))
    shuffle(list1)  # it will shuffle orignal list but it will not return anythin
    if game_input == list1[0]:
        print(f"You Win and correct list is {list1}")
        break
    elif game_input in list1 and game_input != list1[0]:
        print(f"Oops You lose : your correct list is {list1}")
    else:
        print(f"Please enter between number 1 to 3! you have entered {game_input}")

print(randint(4,100)) # randint will return random number from the range that you will define in typle

