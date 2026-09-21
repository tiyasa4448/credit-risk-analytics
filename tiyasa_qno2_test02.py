def calculate_factorial(N):
    # Initialize Nfac to 1
    Nfac = 1

    # Calculate the factorial
    for i in range(1, N + 1):
        Nfac *= i

    return Nfac

def count_digits(number):
    # Convert the number to a string and count the digits
    return len(str(number))

# Input: Take the value of N from the user
N = int(input("Enter the value of N: "))

# Calculate the factorial
Nfac = calculate_factorial(N)

# Count the digits in Nfac
num_digits = count_digits(Nfac)

# Display the results
print(f"{N}! = {Nfac}")
print(f"Total number of digits in {N}! = {num_digits}")
