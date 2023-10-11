'''Writing a new .txt file'''
file = open('my_new_file.txt', 'w')    # Enter any name you want here
file.write('This is my first line.\nThis is my second line.')
file.close() # Important to close the file after writing, reading or appending
Note: If you open an existing file in write mode, the file's contents will
automatically be erased, and you will begin writing to the cleared file.

'''Appending an existing .txt file'''
a = open('my_new_file.txt', 'a')
a.write('\nThis is append mode')
a.close()

'''Using the with statement to automatically close files'''
with open('my_new_file.txt', 'a') as file:
    file.write('\nI am another line through append.')

'''Reading an existing .txt file'''
with open('file.txt', 'r') as f:
    file_contents = f.read()
    print(file_contents)
    words = file_contents.split()
    # Splits file_contents string into a list of words using spaces as separators
    word_count = len(words)
