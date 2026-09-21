# Given lists
names = ["Tom", "Jerry", "Doraemon", "Hattori", "Oggy", "Jack", "Jessie", "James"]
numbers = [91912, 91232, 91213, 91233, 91999, 91929, 91872, 91234]

# Input from the user
name_to_lookup = input("Enter the name to lookup: ")

# Check if the entered name is in the list
if name_to_lookup in names:
    # Find the corresponding number using the index of the name
    index = names.index(name_to_lookup)
    number = numbers[index]
    print(name_to_lookup , "'s number is" , number)
else:
    print(name_to_lookup ,  "is Not Found")
