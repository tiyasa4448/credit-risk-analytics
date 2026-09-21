import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)

while True:
    guess = input("Guess the secret number between 1 and 100 (or type 'quit' to exit): ")

    if guess.lower() == 'quit':
        print("Thanks for playing. The secret number was", secret_number)
        break

    try:
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You guessed the secret number:", secret_number)
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100 or 'quit'.")
