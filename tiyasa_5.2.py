def modify_input(user_input):
    result = ""
    for word in user_input.split():
        modified_word = ""
        for char in word:
            if char.isalpha():
                if char.isupper():
                    modified_char = chr((ord(char) - 65 - 1) % 26 + 65)
                else:
                    modified_char = chr((ord(char) - 97 - 1) % 26 + 97)
            elif char.isdigit():
                modified_char = chr((ord(char) - 48 + 5) % 10 + 48)  # Shift numbers by 5
            else:
                modified_char = char
            modified_word += modified_char

        result += modified_word + " "

    return result.strip()


user_input = input("Enter a sentence: ")
modified_output = modify_input(user_input)
print("Modified Output:", modified_output)
