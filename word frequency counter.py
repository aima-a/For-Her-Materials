def count_word_frequency(sentence):
    word_frequency = {}
    words = sentence.split()
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency
my_sentence = "This is a simple example of a sentence to test if a function is working."
result = count_word_frequency(my_sentence)
print(result)