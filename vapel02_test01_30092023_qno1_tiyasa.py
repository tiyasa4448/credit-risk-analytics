# Prompt the user to enter a temperature in celsius
celsius = float(input("Enter temperature in celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 1.8) + 32

# Display the result
print(celsius, "degrees celsius is equal to" ,  fahrenheit, "degrees fahrenheit.")
# Dispalying the Tempurature according to the condion given,
if fahrenheit <= 32:
    print("IT IS FREEZING")
elif fahrenheit <= 68:
    print("IT IS CHILLY")
elif fahrenheit <= 72:
    print("PLEASANT WEATHER")
else: 
    print("WARM WEATHER")
