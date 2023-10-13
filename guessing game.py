def word(secret_word):
    max_attempts = 10  # Set the maximum number of attempts
    attempts = 0

    while attempts < max_attempts:
        guess = input("Enter your guess: ").lower()  # Convert the guess to lowercase

        if guess == secret_word.lower():  # Make the comparison case-insensitive
            print("Congratulations! You guessed the word correctly.")
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"Incorrect guess. {remaining_attempts} {'attempts' if remaining_attempts > 1 else 'attempt'} left.")

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The secret word was '{secret_word}'.")

secret_word = "password"
word(secret_word)
