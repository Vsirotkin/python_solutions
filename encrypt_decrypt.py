import os

import string
import random
import requests

# Remove punctuation and convert to lowercase
master_sentence = "I go home."
translator = str.maketrans("", "", string.punctuation)
clean_sentence = master_sentence.translate(translator).lower()
DICTIONARY_URL = "https://inventwithpython.com/dictionary.txt"

# Download the dictionary file if it doesn't exist
if not os.path.exists("load_dictionary.txt"):
    response = requests.get(DICTIONARY_URL, timeout=5)
    if response.status_code == 200:
        with open("load_dictionary.txt", "wb") as file:
            file.write(response.content)
    else:
        print("Failed to download the dictionary file")
        exit(1)

# Load the dictionary file and shuffle the lines
with open("load_dictionary.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
random.shuffle(lines)

# Write the shuffled lines to a new file
with open("dictionary_for_encryption.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line)

# Check if any word of clean_sentence is in the load_dictionary.txt
# If not, insert the word in the load_dictionary.txt
with open("load_dictionary.txt", "a+", encoding="utf-8") as file:
    file.seek(0)
    dictionary_words = set(file.read().splitlines())
    for word in clean_sentence.split():
        if word not in dictionary_words:
            file.write(word + "\n")
            dictionary_words.add(word)

# Count the spaces between words in clean_sentence
space_count = clean_sentence.count(" ")

# Prompt the user for inputs
start_point = int(input("Enter the start point: "))
how_many = int(input("Enter how many words to collect for each space: "))
step = int(input("Enter the step (number of words to skip after each collection): "))

# Collect words from dictionary_for_encryption.txt
with open("dictionary_for_encryption.txt", "r", encoding="utf-8") as file:
    words = file.read().splitlines()

# Initialize the list to hold the collected words
collected_words = []

# Use the inputs to collect the required number of words for each space
current_index = start_point
for _ in range(space_count):
    # Collect 'how_many' words starting from the current index
    collected_words.extend(words[current_index : current_index + how_many])
    # Move the current index by 'step' words
    current_index += step

# Insert the collected words into the spaces between words in clean_sentence
split_sentence = clean_sentence.split(" ")
for i in range(space_count):
    # Insert the collected words after the i-th space
    split_sentence.insert(i * 2 + 1, collected_words[i * how_many : (i + 1) * how_many])

# Flatten the list of lists and join into a string
final_sentence_parts = []
for part in split_sentence:
    if isinstance(part, list):
        final_sentence_parts.extend(part)
    else:
        final_sentence_parts.append(part)
final_sentence = " ".join(final_sentence_parts)

# Convert each word in final_sentence to lowercase and reverse it
final_sentence_words = final_sentence.split(" ")
final_sentence_words = [word[::-1].lower() for word in final_sentence_words]
final_sentence = " ".join(final_sentence_words)

# Print the final sentence
print(final_sentence)

# The encrypted sentence from the previous steps
encrypted_final_sentence = final_sentence


# Check if any word of clean_sentence is in the load_dictionary.txt
# If not, insert the word in the load_dictionary.txt
with open("load_dictionary.txt", "a+", encoding="utf-8") as file:
    file.seek(0)
    dictionary_words = set(file.read().splitlines())
    for word in clean_sentence.split():
        if word not in dictionary_words:
            file.write(word + "\n")
            dictionary_words.add(word)

# Load the dictionary file
with open("load_dictionary.txt", "r", encoding="utf-8") as file:
    dictionary_words = set(file.read().splitlines())

# Reverse each word in the encrypted sentence
encrypted_words = encrypted_final_sentence.split(" ")
decrypted_words = [word[::-1] for word in encrypted_words]

# Remove the words that were inserted from the dictionary
decrypted_sentence_parts = []
for word in decrypted_words:
    if word in dictionary_words:
        decrypted_sentence_parts.append(word)

# Reconstruct the sentence without the inserted words
decrypted_sentence = " ".join(decrypted_sentence_parts)

# Print the decrypted sentence
print(decrypted_sentence)