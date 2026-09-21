# Get user input for the number
num = int(input("Enter a number: "))

# Print the multiplication table
for i in range(1, 11):
    result = num * i
    print(num , "*" , i , "=" , result)
