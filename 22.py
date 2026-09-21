#defining functions.
def greater(attempts):
    try:
        guess= float(input("You have guessed a higher number! try again. "))
        attempts += 1
        if guess > target:
            greater(attempts)
        elif guess < target:
            lower(attempts)
        else:
            print("You guessed correctly! congratulations. you got this in ", attempts)
    except ValueError:
        print("Invalid Input! please enter a number.")
        greater(attempts)

def lower(attempts):
    try:
        guess= float(input("You have guessed a lower number! try again. "))
        attempts += 1
        if guess > target:
            greater(attempts)
        elif guess < target:
            lower(attempts)
        else:
            print("You guessed correctly! congratulations. you got this in ", attempts)
    except ValueError:
        print("Invalid Input! please enter a number.")
        lower(attempts)

def start_game(attempts):
    try:
        guess= float(input("Please guess a number between 1 and 100: "))
        attempts += 1
        if guess > target:
            greater(attempts)
        elif guess < target:
            lower(attempts)
        else:
            print("You guessed correctly! congratulations. you got this in ", attempts)
    except ValueError:
        print("Invalid Input! please enter a number.")
        start_game(attempts)

