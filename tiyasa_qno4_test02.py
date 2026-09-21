def calculate_score(sentence):
    # Initialize counters
    total_letters = 0
    total_vowels = 0
    max_vowels = 0

    # Iterate through each word in the sentence
    words = sentence.split()
    for word in words:
        word_letters = sum(c.isalpha() for c in word)
        word_vowels = sum(c.lower() in "aeiou" for c in word)

        total_letters += word_letters
        total_vowels += word_vowels

        # Update max_vowels if the current word has more vowels
        max_vowels = max(max_vowels, word_vowels)

    # Calculate the score
    score = total_letters % (max_vowels + 1)

    return score

# Take input strings until "DONE" is entered
while True:
    input_sentence = input("Enter a sentence (type 'DONE' to finish): ")
    
    if input_sentence.upper() == "DONE":
        break
    
    # Calculate the score for the current sentence
    sentence_score = calculate_score(input_sentence)

    # Display the score for the current sentence
    print(f"Score for '{input_sentence}': {sentence_score}")
