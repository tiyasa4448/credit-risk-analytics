# Get user input
user_input = input("Enter a string: ")

# Initialize a variable to count occurrences
count = 0

# Iterate through the characters in the input string
for char in user_input:
    if char == 'p' or char == 'P':  # Count both lowercase and uppercase 'p'
        count += 1

# Print the result
print("The letter 'p' appears" , count , "times in the input string.")
