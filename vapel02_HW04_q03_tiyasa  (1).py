# Function to check if a number is even or odd
def is_even(input_num): 
    if input_num % 2 == 0:
        return True
       # Input from the user
try:
    input_num = int(input("Enter an integer: "))
    if is_even(input_num):
        print(input_num , "is an EVEN number . ")
    else:
        print(input_num , "is a ODD number .")
except ValueError:
    print("Invalid input. Please enter an integer.")
