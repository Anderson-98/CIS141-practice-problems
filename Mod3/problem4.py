#4. Prompt the user for: a word, a first index, and a last index.
Slice the word at the indexes provided by the user and print to the screen.

# Prompt the user for a word
word = input("Enter a word: ")

# Prompt the user for the first index
first_index = int(input("Enter the first index: "))

# Prompt the user for the last index
last_index = int(input("Enter the last index: "))

# Slice the word using the provided indexes
sliced_word = word[first_index:last_index]

# Print the sliced part of the word
print("The sliced word is:", sliced_word)
