def display_value_and_type(value, name):
    print(name , "Value -" , value , "Type -" , type(value))

def main():
    # Taking inputs
    greeting = input("Enter a simple greeting: ")
    numeric_decimal = float(input("Enter a numeric value with decimal fraction: "))
    numeric_no_decimal = int(input("Enter a numeric value without decimal fraction: "))
    boolean_value = bool(input("Enter a Boolean value (True/False): "))

    # Displaying values and types using the user-defined function
    display_value_and_type(greeting, "Greeting")
    display_value_and_type(numeric_decimal, "Numeric with Decimal")
    display_value_and_type(numeric_no_decimal, "Numeric without Decimal")
    display_value_and_type(boolean_value, "Boolean")

if __name__ == "__main__":
    main()
