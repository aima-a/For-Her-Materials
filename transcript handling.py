with open('transcript.txt', 'r') as file:
    content = file.read()
    # print(content)
    words = content.split()
    word_count = len(words)
    print(f"The word count of my text file is {word_count} words")
