# Open the file in read mode
with open('/Users/aimaanwar/Documents/PyCharm Projects/For Her/Data/transcript.txt', 'r') as file:
    text = file.read()

# 1. Total number of words in the file
words = text.split()
total_words = len(words)

# 2. Total number of characters in the file (not including whitespace)
total_characters = sum(len(word) for word in words)

# 3. The average word length in the file
average_word_length = total_characters / total_words

# 4. The frequency of each word in the file (without using Counter)
word_freq = {}
for word in words:
    word = word.strip('.,!?()-"').lower()
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

# Display the results
print(f"Total number of words: {total_words}")
print(f"Total number of characters (excluding whitespace): {total_characters}")
print(f"Average word length: {average_word_length} characters")
print("\nWord frequency:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
