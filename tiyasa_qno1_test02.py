import random

# Generate a random 10-digit number
random_number = random.randint(10**9, (10**10)-1)

# Convert the number to a string for easy digit extraction
number_str = str(random_number)

# Initialize counters for even and odd digits
even_count = 0
odd_count = 0

# Count the number of even and odd digits
for digit_str in number_str:
    digit = int(digit_str)
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Calculate the percentage of even and odd digits
total_digits = even_count + odd_count
even_percentage = (even_count / total_digits) * 100
odd_percentage = (odd_count / total_digits) * 100

# Print the results
print("Random 10-digit number:", random_number)
print("Even digits:", even_count)
print("Odd digits:", odd_count)
print("Percentage of even digits: {:.2f}%".format(even_percentage))
print("Percentage of odd digits: {:.2f}%".format(odd_percentage))