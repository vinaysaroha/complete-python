from random import shuffle

# from time import sleep

cup = ['', '0', '']


def shuffle_cup():
    shuffle(cup)
    return cup


def guessing_game():
    guess_cup = ''
    while guess_cup not in [1, 2, 3]:
        guess_cup = int(input("guess 1 , 2 , 3 cup in which you think ball is: "))
    return guess_cup - 1


def check_winner_or_not():
    cup = shuffle_cup()
    print(f"{cup}")
    while True:
        user_input = guessing_game()
        if cup[user_input] == '0':
            print("You Win")
            break
        else:
            print("You loos!!! Tyr again !!!")


check_winner_or_not()

