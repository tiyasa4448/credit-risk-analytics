wordlist = [" apple "," plum "," banana "," plum "," apple "," cherry ", " cherry "," mango "," apple "," apple "," cherry "," plum "," banana ", " apple "," apple "," apple "," apple "," banana "," apple "]

# Create an empty dictionary to store word quantities
word_count = {}

# Count the occurrences of each word in the list
for word in wordlist:
    # Remove leading and trailing whitespaces from the word
    cleaned_word = word.strip()
    
    # Update the count in the dictionary
    word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

# Print the words with their quantities
for word, count in word_count.items():
    print(word , ":"  , count)
        