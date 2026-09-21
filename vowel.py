# Get a single character input from the user
char = input("Enter a single character: ")

# Convert the input to lowercase for case-insensitive comparison
char = char.lower()

# Check if the input is a single character and is a letter
if len(char) == 1:
    # Check if the character is a vowel
    if char == ['a', 'e', 'i', 'o', 'u']:
        print(char , "is a vowel.")
    else:
        print(char , "is a consonant.")
else:
    print("Please enter a single alphabetic character.")
