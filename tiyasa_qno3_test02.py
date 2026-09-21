def analyze_sentence(sentence):
    # Initialize counters
    digit_count = 0
    special_char_count = 0
    letter_count = 0

    # Iterate through each character in the sentence
    for char in sentence:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1
        else:
            special_char_count += 1

    # Display the results
    print("Input Sentence:", sentence)
    print("Number of Digits:", digit_count)
    print("Number of Special Characters (including spaces):", special_char_count)
    print("Number of Letters (both uppercase and lowercase):", letter_count)

# Input: Take the sentence from the user
input_sentence = input("Enter a sentence: ")

# Analyze the input sentence
analyze_sentence(input_sentence)
