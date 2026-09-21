# Input from the user
num1 = float(input("Enter the first numeric value: "))
num2 = float(input("Enter the second numeric value: "))
num3 = float(input("Enter the third numeric value: "))

# Initialize variables to store maximum and minimum values
max_value = num1
min_value = num1

# Check and update maximum and minimum values
if num2 > max_value:
    max_value = num2
elif num2 < min_value:
    min_value = num2

if num3 > max_value:
    max_value = num3
elif num3 < min_value:
    min_value = num3

# Display the maximum and minimum values
print("The maximum value is:" , max_value)
print("The minimum value is:" , min_value)
