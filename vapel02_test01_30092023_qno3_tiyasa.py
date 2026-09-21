# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main program
while True:
    # User menu
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    # Get user choice
    choice = input("Enter choice (1/2/3/4/5): ")
    
    if choice == '5':
        print("Exiting the calculator.")
        break
    
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please enter a valid option.")
        continue
    
    # Get user inputs
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
        print("Result: ", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Result: ", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Result: ", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("Result: ", result)
