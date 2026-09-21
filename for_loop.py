#Infinite Loop!

while True:
    user_input=input("Please enter your test")
    if user_input == "Done":
        break
    elif user_input == "":
        continue
    else:
        print(user_input)