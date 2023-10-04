def count_vowels_consonants(input_str):
    # Initialize counts for vowels and consonants
    vowel_count = 0
    consonant_count = 0

    # Loop through each character in the input string
    for char in input_str:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Check if the character is a vowel
            if char.lower() in "aeiou":
                vowel_count += 1
            else:
                consonant_count += 1

    # Print the counts
    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)


def reverse_string(input_str):
    # Reverse the input string using slicing
    reversed_str = input_str[::-1]
    return reversed_str


def remove_spaces(input_str):
    # Remove spaces from the input string using replace()
    no_spaces_str = input_str.replace(" ", "")
    return no_spaces_str


# Main program
while True:
    user_input = input("Enter a string (or 'quit' to exit): ")

    if user_input.lower() == "quit":
        print("Thank you for using the program. Goodbye!")
        break

    print("\nMenu:")
    print("1. Count characters (vowels and consonants)")
    print("2. Reverse string")
    print("3. Remove spaces")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        count_vowels_consonants(user_input)
    elif choice == "2":
        reversed_str = reverse_string(user_input)
        print("Reversed string:", reversed_str)
    elif choice == "3":
        no_spaces_str = remove_spaces(user_input)
        print("String with spaces removed:", no_spaces_str)
    elif choice == "4":
        print("Thank you for using the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.\n")
