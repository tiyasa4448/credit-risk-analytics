# Get user input
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize variables to keep track of the longest word and its length
longest_word = ""
max_length = 0

# Iterate through the words in the sentence
for word in words:
    # Remove any punctuation characters from the word
    word = word.strip(".,?!;:'\"()[]{}")
    
    # Check if the current word is longer than the previously found longest word
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

# Print the longest word and its length
print(f"The longest word is '{longest_word}' with {max_length} letters.")
